# -- coding: UTF-8 --

import os

from cps3_ra_playlist import cps3_lite_rom_list
from game import Game
from games_db import GamesDB
from helper import Helper
from init_global_configs import Init_Global_Configs
from local_configs import LocalConfigs
from pathlib import Path
from ra_playlist_config import LiteRom
from rom import Rom
from roms_db import RomsDB

if __name__ == "__main__":
    Init_Global_Configs()

    doc_path = LocalConfigs.export_to_directory().joinpath(
        f"CPS3 Roms.md",
    )
    if not Helper.verify_exist_directory_ex(doc_path.parent):
        print(f"【错误】无效的目标文件 {doc_path}")
        exit()

    if doc_path.exists() and doc_path.is_file():
        doc_path.unlink()

    with open(doc_path, "w", encoding="utf-8") as doc:
        doc.write(
            "# CPS3 街机游戏兼容性列表\n\n"
            "以 Widows 版的 RetroArch 为例，支持 CPS3 街机游戏的核心不止一个：\n"
            "- Arcade (FB Alpha 2012 CPS-3)\n"
            "- Arcade (FB Alpha 2012)\n"
            "- Arcade (FinalBurn Neo)\n"
            "- Arcade (MAME...) 系列核心\n\n"
            "1G1R 是 1 Game 1 ROM 的缩写，意思是一个游戏只选取一个最佳版本的 ROM 文件。\n\n"
            "下面这份 CPS3 街机游戏列表，是根据 FBNeo - Arcade Games.rdb 数据库里 ROM 文件描述，按照 1G1R 的策略收集整理的，每个 ROM 都支持以下三种核心：\n"
            "1. Arcade (FB Alpha 2012 CPS-3)\n"
            "2. Arcade (FB Alpha 2012)\n"
            "3. Arcade (FinalBurn Neo)\n\n"
            "序号 | ROM 文件 | CRC32 | 依赖于 | 游戏名称\n"
            "--- | --- | --- | --- | ---\n"
        )

        index = 0
        for lite_rom in sorted(cps3_lite_rom_list, key=lambda x: x.file_name):
            rom = RomsDB.query_rom(
                rom_crc32=lite_rom.crc32, rom_file_name=lite_rom.file_name
            )
            game = GamesDB.query_game(game_id=rom.game_id)

            index = index + 1
            parent_rom_msg = " "
            if rom.parent_rom is not None:
                parent_rom_msg = f" {rom.parent_rom.file_name} "
            doc.write(
                f"{index} | {lite_rom.file_name} | {rom.crc32} |{parent_rom_msg}| {game.zhcn_title}\n"
            )

        doc.write(
            "\n**建议优先使用 Arcade (FinalBurn Neo) 核心加载游戏。**\n"
            "\n游戏手柄和街机摇杆的玩家，可以参考下面的做法，避免更换控制器时来回修改按键映射的麻烦：\n"
            "- 使用游戏手柄的时候，选择 Arcade (FinalBurn Neo) 核心，采用游戏手柄的按键映射方案；\n"
            "- 使用街机摇杆的时候，选择 Arcade (FB Alpha 2012) 核心，采用街机摇杆的按键映射方案。\n"
        )

        doc.close()
