# -- coding: UTF-8 --

import os

from helper import Helper
from init_global_configs import Init_Global_Configs
from local_configs import LocalConfigs
from pathlib import Path
from wii_ra_configs import WiiRA_Configs
from wiiflow_configs import WiiFlow_Configs
from wiiflow_game import WiiFlow_Game
from wiiflow_games_db import WiiFlow_GamesDB
from wiiflow_rom import WiiFlow_Rom
from wiiflow_roms_db import WiiFlow_RomsDB

if __name__ == "__main__":
    Init_Global_Configs()

    doc_path = LocalConfigs.export_to_directory().joinpath(
        f"CPS2 Roms.md",
    )
    if not Helper.verify_exist_directory_ex(doc_path.parent):
        print(f"【错误】无效的目标文件 {doc_path}")
        exit()

    if doc_path.exists() and doc_path.is_file():
        doc_path.unlink()

    with open(doc_path, "w", encoding="utf-8") as doc:
        doc.write(
            "# CPS2 街机游戏兼容性列表\n\n"
            "Wii 版的 RetroArch 使用 Arcade (FB Alpha 2012 CPS-2) 核心来加载 CPS2 街机游戏。\n\n\n"
            "## 可玩游戏列表\n\n"
            "序号 | ROM 文件 | CRC32 | 英文名 | 中文名\n"
            "--- | --- | --- | --- | ---\n"
        )

        roms_dir = LocalConfigs.export_to_directory().joinpath(
            WiiRA_Configs.roms_relative_directory()
        )
        index = 0
        for rom_file_name in os.listdir(roms_dir):
            if not WiiFlow_Configs.is_rom_file_name(rom_file_name):
                continue

            index = index + 1
            rom = WiiFlow_RomsDB.query_rom(rom_file_title=Path(rom_file_name).stem)
            game = WiiFlow_GamesDB.query_game(game_id=rom.game_id)
            doc.write(
                f"{index} | {rom_file_name} | {rom.crc32} | {game.en_title} | {game.zhcn_title}\n"
            )

        doc.write(
            "\n\n## 不可玩游戏列表\n\n"
            "序号 | ROM 文件 | 英文名 | 中文名 | 问题描述\n"
            "--- | --- | --- | --- | ---\n"
        )

        rom_file_name_to_bug_dict = {
            "mmancp2u.zip": "无法运行",
        }
        index = 0
        for rom_file_name, bug in rom_file_name_to_bug_dict.items():
            index = index + 1
            rom = WiiFlow_RomsDB.query_rom(rom_file_title=Path(rom_file_name).stem)
            game = WiiFlow_GamesDB.query_game(game_id=rom.game_id)
            doc.write(
                f"{index} | {rom_file_name} | {game.en_title} | {game.zhcn_title} | {bug}\n"
            )

        doc.close()
