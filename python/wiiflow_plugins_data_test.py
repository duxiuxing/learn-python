# -- coding: UTF-8 --

import xml.etree.ElementTree as ET

from init_global_configs import Init_Global_Configs
from local_configs import LocalConfigs
from wiiflow_configs import WiiFlow_Configs
from wiiflow_games_db import WiiFlow_GamesDB
from wiiflow_plugins_data import WiiFlow_PluginsData


if __name__ == "__main__":
    Init_Global_Configs()

    game_list_elem = ET.Element("GameList")

    game_list = sorted(WiiFlow_GamesDB.all_games(), key=lambda x: x.name)
    for game in game_list:
        ET.SubElement(
            game_list_elem,
            "Game",
            {"id": game.id, "en_title": game.en_title, "zhcn_title": game.zhcn_title},
        )

    plugin_name = WiiFlow_Configs.plugin_name()
    rom_xml_file_path = LocalConfigs.repository_directory().joinpath(
        f"wii\\wiiflow\\plugins_data\\{plugin_name}\\roms.xml"
    )

    ET.ElementTree(game_list_elem).write(
        rom_xml_file_path, encoding="utf-8", xml_declaration=True
    )
