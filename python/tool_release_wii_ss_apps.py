# -- coding: UTF-8 --

import os
import xml.etree.ElementTree as ET

from helper import Helper
from init_global_configs import Init_Global_Configs
from local_configs import LocalConfigs
from pathlib import Path
from wii_app_info import Wii_AppInfo
from wii_ss_configs import WiiSS_Configs
from wiiflow_configs import WiiFlow_Configs
from wiiflow_game import WiiFlow_Game
from wiiflow_games_db import WiiFlow_GamesDB
from wiiflow_rom import WiiFlow_Rom
from wiiflow_roms_db import WiiFlow_RomsDB

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

    while True:
        index = 0
        index_to_app_info_dict = {}
        for app_info in sorted(app_info_list, key=lambda x: x.game_zhcn_title):
            index = index + 1
            index_to_app_info_dict[index] = app_info
            print(f"{index}. {app_info.game_zhcn_title}")

        user_input = input(
            "请输入要发布的 App 的序号，并按回车确认，直接回车表示退出 > "
        )

        try:
            number = int(user_input)
            if number not in index_to_app_info_dict.keys():
                break
            app_info = index_to_app_info_dict[number]
            rom_file_title = Path(app_info.rom_file_name).stem
            device = app_info.folder_name[: app_info.folder_name.find("-")].upper()
            dst_root_dir = Path(
                f"{LocalConfigs.export_to_directory}-apps-release\\{device}-{WiiFlow_Configs.plugin_name}"
                f"-{str(number).rjust(2, '0')}-{app_info.game_zhcn_title[4:]}-SS核心"
            )
            if not Helper.verify_exist_directory_ex(dst_root_dir):
                print(f"【错误】无效的目录：{dst_root_dir}")
                break

            # 拷贝 apps 目录里的 App 文件夹
            src_app_dir = LocalConfigs.export_to_directory.joinpath(
                f"apps\\{app_info.folder_name}"
            )
            dst_app_dir = dst_root_dir.joinpath(f"apps\\{app_info.folder_name}")
            Helper.copy_directory(src_app_dir, dst_app_dir)

            # 拷贝 private 目录里的 .cfg 文件
            src_cfg_file_path = LocalConfigs.export_to_directory.joinpath(
                f"private\\{WiiSS_Configs.data_folder_name}\\{rom_file_title}.cfg"
            )
            Helper.copy_file_to_directory(
                src_cfg_file_path,
                dst_root_dir.joinpath(f"private\\{WiiSS_Configs.data_folder_name}"),
            )

            # 拷贝 wad 文件
            src_wad_file_path_list = []
            src_wad_dir = LocalConfigs.repository_directory.joinpath(
                f"wii\\wad\\{rom_file_title}"
            )
            if src_wad_dir.exists() and src_wad_dir.is_dir():
                for file_path in src_wad_dir.glob("*.wad"):
                    src_wad_file_path_list.append(file_path)
            if len(src_wad_file_path_list) == 0:
                print(f"【警告】未发现 App 对应的 .wad 文件：{src_wad_dir}")
            else:
                dst_dir = dst_root_dir.joinpath(
                    f"wad\\{WiiFlow_Configs.plugin_name.lower()}"
                )
                if not Helper.verify_exist_directory_ex(dst_dir):
                    print(f"【错误】无效的目录：{dst_dir}")
                else:
                    for src_file_path in src_wad_file_path_list:
                        Helper.copy_file_to_directory(src_file_path, dst_dir)

            print(
                f"\n{app_info.game_zhcn_title[4:]} App 的相关文件已经拷贝至：\n{dst_root_dir}\n\n"
            )
        except ValueError:
            break
