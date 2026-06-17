# -- coding: UTF-8 --

import os
import xml.etree.ElementTree as ET

from game import Game
from games_db import GamesDB
from helper import Helper
from init_global_configs import Init_Global_Configs
from local_configs import LocalConfigs
from resource_file_helper import ResourceFileHelper
from rom import Rom
from roms_db import RomsDB
from wiiflow_configs import WiiFlow_Configs
from wiiflow_game import WiiFlow_Game
from wiiflow_games_db import WiiFlow_GamesDB
from wiiflow_rom import WiiFlow_Rom
from wiiflow_roms_db import WiiFlow_RomsDB


def f1_generate_roms_xml():
    plugin_name = WiiFlow_Configs.plugin_name
    roms_xml_path = LocalConfigs.repository_directory.joinpath(
        f"wii\\wiiflow\\plugins_data\\{plugin_name}\\roms.xml"
    )
    if roms_xml_path.exists() and roms_xml_path.is_file():
        roms_xml_path.unlink()

    game_list_elem = ET.Element("GameList")
    game_list = sorted(WiiFlow_GamesDB.all_games(), key=lambda x: x.name)
    for game in game_list:
        ET.SubElement(
            game_list_elem,
            "Game",
            {"id": game.id, "en_title": game.en_title, "zhcn_title": game.zhcn_title},
        )

    ET.ElementTree(game_list_elem).write(
        roms_xml_path, encoding="utf-8", xml_declaration=True
    )


def f2_print_games_by_genre():
    en_genre_list = []
    en_genre_to_game_list = {}

    for game in WiiFlow_GamesDB.all_games():
        if game.en_genre in en_genre_to_game_list.keys():
            en_genre_to_game_list[game.en_genre].append(game)
        else:
            en_genre_list.append(game.en_genre)
            en_genre_to_game_list[game.en_genre] = [game]

    for en_genre in sorted(en_genre_list):
        game_list = en_genre_to_game_list[en_genre]
        print(f"{en_genre} x {len(game_list)}")
        index = 0
        for game in sorted(game_list, key=lambda x: x.name):
            index = index + 1
            print(f"  {game.zhcn_genre}\t{index}\t{game.zhcn_title}    {game.en_title}")


def f3_print_games_by_en_title():
    game_list = sorted(WiiFlow_GamesDB.all_games(), key=lambda x: x.en_title)
    for game in game_list:
        print(game.en_title)


def f4_print_roms_by_en_title():
    game_list = sorted(WiiFlow_GamesDB.all_games(), key=lambda x: x.en_title)
    for game in game_list:
        rom = WiiFlow_RomsDB.query_rom(game_id=game.id)
        print(f'"{rom.file_title}",')


def f5_print_roms_by_rom_file():
    rom_list = []
    for game in WiiFlow_GamesDB.all_games():
        rom_list.append(WiiFlow_RomsDB.query_rom(game_id=game.id))

    print("    rom_file_title_list = [")
    for rom in sorted(rom_list, key=lambda x: x.file_title):
        print(f'        "{rom.file_title}",')
    print("    ]")


def f6_print_rom_and_en_title_by_rom_file():
    rom_list = []
    for game in WiiFlow_GamesDB.all_games():
        rom_list.append(WiiFlow_RomsDB.query_rom(game_id=game.id))

    for rom in sorted(rom_list, key=lambda x: x.file_title):
        game = WiiFlow_GamesDB.query_game(game_id=rom.game_id)
        print(
            f'    Wii_AppFactory.add_game_app_configs(rom_file_title="{rom.file_title}", app_name="{game.en_title}")'
        )


def f7_check_game_element():
    plugin_name = WiiFlow_Configs.plugin_name
    wiiflow_all_games = WiiFlow_GamesDB.all_games()
    print(f"在 {plugin_name}.xml 中发现 {len(wiiflow_all_games)} 个游戏")
    for wiiflow_game in wiiflow_all_games:
        game = GamesDB.query_game(game_id=wiiflow_game.id)
        if game is None:
            print(
                f"【错误】{plugin_name}.xml 中的 <Game> 没有在 roms.xml 中配置："
                f"id = {wiiflow_game.id}，en_title = {wiiflow_game.en_title}"
            )
            continue

        en_title_match = game.en_title == wiiflow_game.en_title
        zhcn_title_match = game.zhcn_title == wiiflow_game.zhcn_title

        if en_title_match and zhcn_title_match:
            print(f"roms.xml 中的 <Game> 匹配：{game.en_title}，{game.zhcn_title}")
            continue

        en_title_msg = ""
        if en_title_match:
            en_title_msg = f"\n\ten_title = {game.en_title}"
        else:
            en_title_msg = (
                f"\n\ten_title 不一致\n"
                f"\t\troms.xml: {game.en_title}\n"
                f"\t\tWiiFlow: {wiiflow_game.en_title}"
            )

        zhcn_title_msg = ""
        if zhcn_title_match is False:
            zhcn_title_msg = (
                f"\n\tzhcn_title 不一致\n"
                f"\t\troms.xml: {game.zhcn_title}\n"
                f"\t\tWiiFlow: {wiiflow_game.zhcn_title}"
            )

        print(
            f"【错误】roms.xml 中的 <Game> 不匹配：id = {game.id}"
            f"{en_title_msg}{zhcn_title_msg}"
        )


def f8_check_rom_element():
    plugin_name = WiiFlow_Configs.plugin_name
    wiiflow_all_roms = WiiFlow_RomsDB.all_roms()
    print(f"在 {plugin_name}.ini 中发现 {len(wiiflow_all_roms)} 个 ROM 文件")
    all_roms_match = True
    for wiiflow_rom in wiiflow_all_roms:
        rom = RomsDB.query_rom(rom_crc32=wiiflow_rom.crc32)
        if rom is None:
            print(
                f"【错误】{plugin_name}.ini 中的 ROM 文件没有在 roms.xml 中配置："
                f"id = {wiiflow_rom.game_id}，rom_file_title = {wiiflow_rom.file_title}, rom_crc32 = {wiiflow_rom.crc32}"
            )
            continue

        rom_file_path = ResourceFileHelper.compute_rom_file_path(
            rom, include_crc32=True
        )
        rom_file_exists = rom_file_path.exists()

        if not rom_file_exists:
            rom_file_path = ResourceFileHelper.compute_rom_file_path(
                rom, include_crc32=False
            )
            rom_file_exists = rom_file_path.exists()

        if not rom_file_exists:
            print(f"【错误】缺失 ROM 文件 {rom_file_path}")
            all_roms_match = False
            continue

        rom_crc32 = Helper.compute_crc32(rom_file_path)
        rom_crc32_match = rom_crc32 == rom.crc32

        rom_bytes = str(os.stat(rom_file_path).st_size)
        rom_bytes_match = rom_bytes == rom.bytes

        if rom_crc32_match and rom_bytes_match:
            continue

        all_roms_match = False
        rom_crc32_msg = ""
        if not rom_crc32_match:
            rom_crc32_msg = (
                f"\n\tcrc32 不匹配\n" f"\t\t实际值 = {rom_crc32}，预期值 = {rom.crc32}"
            )

        rom_bytes_msg = ""
        if not rom_bytes_match:
            rom_bytes_msg = (
                f"\n\tbytes 不匹配\n" f"\t\t实际值 = {rom_bytes}，预期值 = {rom.bytes}"
            )

        print(
            f"【错误】roms.xml 中的 <Rom> 校验失败：file_name = {rom.file_name}"
            f"{rom_crc32_msg}{rom_bytes_msg}"
        )

    if all_roms_match:
        print("所有 ROM 文件的 crc32 和 bytes 都匹配")


if __name__ == "__main__":
    Init_Global_Configs()

    while True:
        print(
            f"\n1. 依据 {WiiFlow_Configs.plugin_name}.xml 生成 roms.xml\n"
            "2. 依据类型打印游戏列表\n"
            "3. 依据 en_title 音序打印列表\n"
            "4. 依据 en_title 音序打印 ROM 文件列表\n"
            "5. 依据 ROM 文件音序打印文件列表\n"
            "6. 依据 ROM 文件音序打印文件名和 en_title 列表\n"
            f"7. 检查 {WiiFlow_Configs.plugin_name}.xml 和 rom.xml 里面的游戏名称\n"
            f"8. 检查 {WiiFlow_Configs.plugin_name}.ini 和 rom.xml 里面的 crc32 和 bytes\n"
            "其他输入表示退出\n"
        )
        user_input = input("请输入操作的序号 > ")
        try:
            number = int(user_input)
            if number == 1:
                f1_generate_roms_xml()
            elif number == 2:
                f2_print_games_by_genre()
            elif number == 3:
                f3_print_games_by_en_title()
            elif number == 4:
                f4_print_roms_by_en_title()
            elif number == 5:
                f5_print_roms_by_rom_file()
            elif number == 6:
                f6_print_rom_and_en_title_by_rom_file()
            elif number == 7:
                f7_check_game_element()
            elif number == 8:
                f8_check_rom_element()
            else:
                break
        except ValueError:
            break
