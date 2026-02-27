# -- coding: UTF-8 --

import xml.etree.ElementTree as ET

from init_global_configs import Init_Global_Configs
from local_configs import LocalConfigs
from wiiflow_configs import WiiFlow_Configs
from wiiflow_game import WiiFlow_Game
from wiiflow_games_db import WiiFlow_GamesDB
from wiiflow_plugins_data import WiiFlow_PluginsData


def generate_roms_xml():
    plugin_name = WiiFlow_Configs.plugin_name()
    roms_xml_path = LocalConfigs.repository_directory().joinpath(
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


def print_games_by_genre():
    genre_list = []
    genre_to_game_list = {}

    for game in WiiFlow_GamesDB.all_games():
        if game.genre in genre_to_game_list.keys():
            genre_to_game_list[game.genre].append(game)
        else:
            genre_list.append(game.genre)
            genre_to_game_list[game.genre] = [game]

    for genre in sorted(genre_list):
        print(genre)
        for game in sorted(genre_to_game_list[genre], key=lambda x: x.name):
            print(f"\ten = {game.en_title}, zhcn = {game.zhcn_title}")


if __name__ == "__main__":
    Init_Global_Configs()

    while True:
        print(f"\n1. 根据 {WiiFlow_Configs.plugin_name()}.xml 生成 roms.xml")
        print("2. 打印游戏分类列表")
        print("其他输入表示退出")
        user_input = input("请输入操作的序号 > ")
        try:
            number = int(user_input)
            if number == 1:
                generate_roms_xml()
            elif number == 2:
                print_games_by_genre()
            else:
                break
        except ValueError:
            break
