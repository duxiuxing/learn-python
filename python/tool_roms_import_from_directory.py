# -- coding: UTF-8 --

import fnmatch
import os

from game import Game
from games_db import GamesDB
from helper import Helper
from init_global_configs import Init_Global_Configs
from local_configs import LocalConfigs
from pathlib import Path
from resource_file_helper import ResourceFileHelper
from rom import Rom
from roms_db import RomsDB
from wiiflow_configs import WiiFlow_Configs
from wiiflow_game import WiiFlow_Game
from wiiflow_games_db import WiiFlow_GamesDB
from wiiflow_rom import WiiFlow_Rom
from wiiflow_roms_db import WiiFlow_RomsDB


if __name__ == "__main__":
    Init_Global_Configs()

    src_dir = None
    while True:
        src_dir = LocalConfigs.import_from_directory().joinpath(
            f"games\\{WiiFlow_Configs.plugin_name().lower()}-import"
        )
        print("\n即将导入源文件夹里的 ROM 文件")
        print(f"默认源文件夹路径：{src_dir}")
        user_input = input("请确认源文件夹路径，使用默认路径请直接按回车 > ")
        if len(user_input) > 0:
            src_dir = Path(user_input)

        if src_dir.exists() and src_dir.is_dir():
            break
        else:
            print(f"【错误】无效的源文件夹路径：{src_dir}")
            continue

    exist_rom_file_name_to_crc32_to_dict = {}
    new_roms_count = 0
    for rom_file_name in os.listdir(src_dir):
        if not fnmatch.fnmatch(
            rom_file_name, f"*{WiiFlow_Configs.rom_file_extension()}"
        ):
            continue

        src_rom_file_path = src_dir.joinpath(rom_file_name)
        rom_crc32 = Helper.compute_crc32(src_rom_file_path)
        if RomsDB.rom_exist(rom_crc32):
            exist_rom_file_name_to_crc32_to_dict[rom_file_name] = rom_crc32
            continue

        wiiflow_rom = WiiFlow_RomsDB.query_rom(
            rom_crc32=rom_crc32, rom_file_title=Path(rom_file_name).stem
        )
        if wiiflow_rom is None:
            print(f"【提示】未知的 ROM 文件：{rom_file_name} crc32={rom_crc32}")
            continue

        wiiflow_game = WiiFlow_GamesDB.query_game(game_id=wiiflow_rom.game_id)
        print(
            f'    <Game id="{wiiflow_game.id}"\n'
            f'        en_title="{wiiflow_game.en_title}"\n'
            f'        zhcn_title="{wiiflow_game.zhcn_title}"\n'
            '        hfsplay="" launchbox="">'
        )

        rom_bytes = str(src_rom_file_path.stat().st_size)
        print(
            f'        <Rom crc32="{rom_crc32}" bytes="{rom_bytes}"\n'
            f'            file_name="{rom_file_name}"\n'
            '            en_title=""\n'
            '            zhcn_title=""\n'
            '            cores-work="" cores-not-work=""\n'
            "        />\n"
            "    </Game>"
        )

        print(f"导入 ROM 文件：{rom_file_name} crc32={rom_crc32}")
        game = GamesDB.query_game(game_id=wiiflow_game.id)
        if game is None:
            game = Game(
                id=wiiflow_game.id,
                en_title=wiiflow_game.en_title,
                zhcn_title=wiiflow_game.zhcn_title,
            )
            GamesDB.add_game(game)

        rom = Rom(
            game_id=game.id,
            crc32=rom_crc32,
            bytes=rom_bytes,
            file_name=rom_file_name,
            parent_rom=None,
            en_title="",
            zhcn_title="",
        )
        if WiiFlow_Configs.rom_file_renameable():
            rom.file_name = (
                f"{wiiflow_rom.file_title}{WiiFlow_Configs.rom_file_extension()}"
            )
        RomsDB.add_rom(rom)

        dst_rom_file_path = ResourceFileHelper.compute_rom_file_path(
            rom=rom, include_crc32=False
        )
        if dst_rom_file_path.exists() and dst_rom_file_path.is_file():
            dst_rom_file_path = ResourceFileHelper.compute_rom_file_path(
                rom=rom, include_crc32=True
            )
            if dst_rom_file_path.exists() and dst_rom_file_path.is_file():
                print("【错误】ROM 文件已经存在，但未在 .xml 文件中配置")
                continue

        if Helper.verify_exist_directory_ex(dst_rom_file_path.parent):
            Helper.copy_file_if_not_exist(src_rom_file_path, dst_rom_file_path)
            print(f"\t{rom_file_name} -> {dst_rom_file_path}")
            new_roms_count = new_roms_count + 1

    if new_roms_count == 0:
        print("无新游戏导入")
    else:
        print(f"已导入 {new_roms_count} 个新游戏")

    exist_roms_count = len(exist_rom_file_name_to_crc32_to_dict)
    if exist_roms_count > 0:
        print(f"【提示】下列 ROM 文件已经存在，无需导入（共 {exist_roms_count} 个）：")
        for rom_file_name, rom_crc32 in exist_rom_file_name_to_crc32_to_dict.items():
            print(f"\t{rom_file_name} crc32={rom_crc32}")
