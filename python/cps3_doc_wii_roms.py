# -- coding: UTF-8 --

import os

from helper import Helper
from init_global_configs import Init_Global_Configs
from local_configs import LocalConfigs
from pathlib import Path
from ra_configs import RA_Configs
from wii_ra_configs import WiiRA_Configs
from wiiflow_configs import WiiFlow_Configs
from wiiflow_game import WiiFlow_Game
from wiiflow_games_db import WiiFlow_GamesDB
from wiiflow_rom import WiiFlow_Rom
from wiiflow_roms_db import WiiFlow_RomsDB

# https://github.com/R-Sam-1980/cps3 的 wii-roms 分支
if __name__ == "__main__":
    Init_Global_Configs()

    doc_path = LocalConfigs.export_to_directory.joinpath(
        f"{WiiFlow_Configs.plugin_name} Roms (Wii).md",
    )
    if doc_path.exists() and doc_path.is_file():
        doc_path.unlink()

    with open(doc_path, "w", encoding="utf-8") as doc:
        doc.write(
            f"# {WiiFlow_Configs.plugin_name} 街机游戏兼容性列表\n\n"
            f"Wii 版的 RetroArch 使用以下核心来加载 {WiiFlow_Configs.plugin_name} 街机游戏：\n"
            f"- 核心名称：{WiiRA_Configs.core_name}\n"
            f"- 核心文件：{WiiRA_Configs.core_file_name}\n\n\n"
            "## 可玩游戏列表\n\n"
            "序号 | ROM 文件 | CRC32 | 英文名 | 中文名\n"
            "--- | --- | --- | --- | ---\n"
        )

        roms_dir = LocalConfigs.export_to_directory.joinpath(
            RA_Configs.wii_roms_relative_directory
        )
        index = 0
        for rom_file_name in os.listdir(roms_dir):
            if not WiiFlow_Configs.is_rom_file_name(rom_file_name):
                continue

            index = index + 1
            rom = WiiFlow_RomsDB.query_rom(rom_file_title=Path(rom_file_name).stem)
            game = WiiFlow_GamesDB.query_game(game_id=rom.game_id)
            doc.write(
                f"{index} | {rom_file_name} | {rom.crc32} | {game.en_title} | {game.zhcn_title[4:]}\n"
            )

        doc.write(
            "\n虽然 Wii 的推出时间比 CPS3 晚了将近 10 年，但是以 Wii 的机能，还有模拟器目前的优化程度，"
            "还达不到“完美运行” CPS3 街机游戏的标准。Wii 版的 RetroArch 可以通过跳帧（Frameskip）来换取游戏流畅度，"
            "所以，如果你只是想尝鲜一下，Wii 是一个可行的选择，但如果想要追求完美体验，建议还是选择其他更高性能的设备吧。\n"
        )

        doc.close()
