# -- coding: UTF-8 --

import xml.etree.ElementTree as ET

from game import Game
from games_db import GamesDB
from helper import Helper
from local_configs import LocalConfigs
from pathlib import Path
from rom import Rom
from roms_db import RomsDB


class RomsXML:
    @staticmethod
    def _parse(xml_file_path: Path):
        if not xml_file_path.exists() or not xml_file_path.is_file():
            return

        game_list_elem = ET.parse(xml_file_path).getroot()

        for game_elem in game_list_elem.findall("Game"):
            game = Game(
                id=game_elem.attrib["id"],
                en_title=game_elem.attrib["en_title"],
                zhcn_title=game_elem.get("zhcn_title"),
            )
            GamesDB.add_game(game)

            for rom_elem in game_elem.findall("Rom"):
                rom = Rom(
                    file_name=rom_elem.attrib["file_name"],
                    crc32=rom_elem.attrib["crc32"].rjust(8, "0"),
                )
                rom.bytes = rom_elem.attrib["bytes"]
                rom.game_id = game.id
                rom.parent_rom = RomsDB.query_rom(
                    rom_crc32=rom_elem.get("parent_rom_crc32"),
                    rom_file_name=rom_elem.get("parent_rom_file"),
                )
                rom.en_title = rom_elem.attrib["en_title"]
                rom.zhcn_title = game_elem.get("zhcn_title")

                RomsDB.add_rom(rom)
                game.rom_list.append(rom)

    def __init__(self):
        repository_dir = LocalConfigs.repository_directory
        if Helper.files_in_letter_folder():
            for letter in "#ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                xml_file_path = repository_dir.joinpath(f"roms\\{letter}\\{letter}.xml")
                RomsXML._parse(xml_file_path)
        else:
            xml_file_path = repository_dir.joinpath("roms\\roms.xml")
            RomsXML._parse(xml_file_path)
