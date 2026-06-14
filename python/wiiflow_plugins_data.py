# -- coding: UTF-8 --

import os
import xml.etree.ElementTree as ET

from configparser import ConfigParser
from helper import Helper
from local_configs import LocalConfigs
from pathlib import Path
from wiiflow_configs import WiiFlow_Configs
from wiiflow_game import WiiFlow_Game
from wiiflow_games_db import WiiFlow_GamesDB
from wiiflow_rom import WiiFlow_Rom
from wiiflow_roms_db import WiiFlow_RomsDB


class WiiFlow_PluginsData:
    @staticmethod
    def _parse_xml_file():
        plugin_name = WiiFlow_Configs.plugin_name
        xml_file_path = LocalConfigs.repository_directory.joinpath(
            f"wii\\wiiflow\\plugins_data\\{plugin_name}\\{plugin_name}.xml"
        )

        if not xml_file_path.exists():
            print(f"【错误】无效的文件 {xml_file_path}")
            return

        tree = ET.parse(xml_file_path)
        root_elem = tree.getroot()

        for game_elem in root_elem.findall("game"):
            game_name = game_elem.attrib["name"]
            game_id = ""
            en_title = ""
            zhcn_title = ""
            developer = ""
            publisher = ""
            en_genre = ""
            zhcn_genre = ""
            date = ""
            players = ""

            for elem in game_elem:
                if elem.tag == "id":
                    game_id = elem.text
                elif elem.tag == "locale":
                    lang = elem.get("lang")
                    if lang == "EN":
                        en_title = elem.find("title").text
                        if en_title != game_name:
                            print("【警告】英文名不一致")
                            print(f"\tname\t= {game_name}")
                            print(f"\ttitle\t= {en_title}")
                        genre_elem = elem.find("genre")
                        if genre_elem is not None:
                            en_genre = genre_elem.text
                    elif lang == "ZHCN":
                        zhcn_title = elem.find("title").text
                        genre_elem = elem.find("genre")
                        if genre_elem is not None:
                            zhcn_genre = genre_elem.text
                elif elem.tag == "developer":
                    developer = elem.text
                elif elem.tag == "publisher":
                    publisher = elem.text
                elif elem.tag == "date":
                    year = elem.attrib["year"]
                    month = elem.attrib["month"]
                    if len(month) == 0:
                        date = year
                    else:
                        day = elem.attrib["day"]
                        if len(day) == 0:
                            date = f"{year}-{month}"
                        else:
                            date = f"{year}-{month}-{day}"
                elif elem.tag == "input":
                    players = elem.attrib["players"]

            game = WiiFlow_Game(
                name=game_name,
                id=game_id,
                en_title=en_title,
                zhcn_title=zhcn_title,
                developer=developer,
                publisher=publisher,
                en_genre=en_genre,
                zhcn_genre=zhcn_genre,
                date=date,
                players=players,
            )
            WiiFlow_GamesDB.add_game(game)

    @staticmethod
    def _parse_ini_file():
        plugin_name = WiiFlow_Configs.plugin_name
        ini_file_path = LocalConfigs.repository_directory.joinpath(
            f"wii\\wiiflow\\plugins_data\\{plugin_name}\\{plugin_name}.ini"
        )

        if not ini_file_path.exists():
            print(f"【错误】无效的文件 {ini_file_path}")
            return

        ini_parser = ConfigParser()
        ini_parser.read(ini_file_path)
        if ini_parser.has_section(plugin_name):
            for rom_file_title in ini_parser[plugin_name]:
                values = ini_parser[plugin_name][rom_file_title].split("|")
                game_id = values[0]

                for index in range(1, len(values) - 1):
                    rom_crc32 = values[index].rjust(8, "0")
                    rom = WiiFlow_Rom(
                        game_id=game_id,
                        crc32=rom_crc32,
                        file_title=rom_file_title,
                    )
                    WiiFlow_RomsDB.add_rom(rom)

    def __init__(self):
        WiiFlow_PluginsData._parse_xml_file()
        WiiFlow_PluginsData._parse_ini_file()
