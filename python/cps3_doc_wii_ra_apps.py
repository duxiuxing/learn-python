# -- coding: UTF-8 --

import os
import xml.etree.ElementTree as ET

from helper import Helper
from init_global_configs import Init_Global_Configs
from local_configs import LocalConfigs
from pathlib import Path
from wii_app_configs import Wii_AppConfigs
from wii_app_info import Wii_AppInfo
from wii_ra_configs import WiiRA_Configs
from wiiflow_configs import WiiFlow_Configs
from wiiflow_game import WiiFlow_Game
from wiiflow_games_db import WiiFlow_GamesDB
from wiiflow_rom import WiiFlow_Rom
from wiiflow_roms_db import WiiFlow_RomsDB

# https://github.com/R-Sam-1980/cps3 的 wii-ra-apps-sd 分支
# 生成文档 CPS3 Apps (RetroArch).md
if __name__ == "__main__":
    Init_Global_Configs()

    app_info_list = []
    apps_dir = LocalConfigs.export_to_directory.joinpath("apps")
    for app_folder_name in os.listdir(apps_dir):
        meta_xml_path = apps_dir.joinpath(f"{app_folder_name}\\meta.xml")
        if not meta_xml_path.exists() or not meta_xml_path.is_file():
            continue

        app_info = Wii_AppInfo(app_folder_name)
        tree = ET.parse(meta_xml_path)
        root_elem = tree.getroot()
        for elem in root_elem:
            if elem.tag == "name":
                app_info.name = elem.text
            elif elem.tag == "arguments":
                for arg_elem in elem.findall("arg"):
                    if WiiFlow_Configs.is_rom_file_name(arg_elem.text):
                        app_info.rom_file_name = arg_elem.text
                        rom = WiiFlow_RomsDB.query_rom(
                            rom_file_title=Path(arg_elem.text).stem
                        )
                        game = WiiFlow_GamesDB.query_game(game_id=rom.game_id)
                        app_info.game_zhcn_title = game.zhcn_title

        if app_info.rom_file_name is not None:
            app_info_list.append(app_info)

    doc_path = LocalConfigs.export_to_directory.joinpath(
        "CPS3 Apps (RA核心，SD卡版).md",
    )
    if not Helper.verify_exist_directory_ex(doc_path.parent):
        print(f"【错误】无效的目标文件 {doc_path}")
        exit()
    if doc_path.exists() and doc_path.is_file():
        doc_path.unlink()

    with open(doc_path, "w", encoding="utf-8") as doc:
        doc.write(
            "# CPS3 街机游戏 App 列表\n\n"
            "1G1R1A 是 one Game one ROM one App 的缩写，意思是一个游戏只选取一个版本的 ROM 文件，同时还有一个独立的 App 专门负责加载这个游戏的 ROM 文件。\n\n"
            "以下这些 CPS3 街机游戏 App，基于 Wii 版 RetroArch 的 CPS3 核心（fbalpha2012_cps3_libretro_wii.dol）制作，必须和游戏 ROM 文件一起放置在 SD 卡才能正常运行：\n\n"
            "## 按 App 名称排序\n\n"
            "序号 | App 名称 | App 图标 | 游戏中文名 | ROM 文件\n"
            "--- | --- | --- | --- | ---\n"
        )

        index = 0
        for app_info in sorted(app_info_list, key=lambda x: x.name):
            index = index + 1
            doc.write(
                f"{index} | {app_info.name} | ![](./apps/{app_info.folder_name}/icon.png) | {app_info.game_zhcn_title[4:]} | {app_info.rom_file_name}\n"
            )

        doc.write(
            "\n\n## 按游戏中文名排序\n\n"
            "序号 | 游戏中文名 | App 图标 | App 名称 | ROM 文件\n"
            "--- | --- | --- | --- | ---\n"
        )

        index = 0
        for app_info in sorted(app_info_list, key=lambda x: x.game_zhcn_title):
            index = index + 1
            doc.write(
                f"{index} | {app_info.game_zhcn_title} | ![](./apps/{app_info.folder_name}/icon.png) | {app_info.name} | {app_info.rom_file_name}\n"
            )
        doc.close()
