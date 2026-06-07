# -- coding: UTF-8 --

import xml.etree.ElementTree as ET

from init_global_configs import Init_Global_Configs
from local_configs import LocalConfigs
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
        print(en_genre)
        for game in sorted(en_genre_to_game_list[en_genre], key=lambda x: x.name):
            print(
                f"\t{game.zhcn_genre}\tzhcn = {game.zhcn_title}, en = {game.en_title}"
            )


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
            f'    add_game_app_configs(rom_file_title="{rom.file_title}", app_name="{game.en_title}")'
        )


if __name__ == "__main__":
    Init_Global_Configs()

    while True:
        print(f"\n1. 依据 {WiiFlow_Configs.plugin_name}.xml 生成 roms.xml")
        print("2. 依据类型打印游戏列表")
        print("3. 依据 en_title 音序打印列表")
        print("4. 依据 en_title 音序打印 ROM 文件列表")
        print("5. 依据 ROM 文件音序打印文件列表")
        print("6. 依据 ROM 文件音序打印文件名和 en_title 列表")
        print("其他输入表示退出")
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
            else:
                break
        except ValueError:
            break
