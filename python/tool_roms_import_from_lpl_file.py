# -- coding: UTF-8 --

import fnmatch
import json
import os

from game import Game
from games_db import GamesDB
from helper import Helper
from init_global_configs import Init_Global_Configs
from local_configs import LocalConfigs
from pathlib import Path
from ra_configs import RA_Configs
from ra_rom import RA_Rom
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

    lpl_file_path = None
    while True:
        lpl_file_path = LocalConfigs.retroarch_directory().joinpath(
            "playlists", RA_Configs.lpl_file_name()
        )
        print("\n即将根据 .lpl 文件导入 ROM 文件")
        print(f"默认 .lpl 文件路径：{lpl_file_path}")
        user_input = input("请输入 .lpl 文件路径，使用默认路径请直接按回车 > ")
        if len(user_input) > 0:
            lpl_file_path = Path(user_input)

        if lpl_file_path.exists() and lpl_file_path.is_file():
            break
        else:
            print(f"【错误】无效的文件路径：{lpl_file_path}")

    ra_rom_list = []
    with open(lpl_file_path, "r", encoding="utf-8") as file:
        items = json.load(file)["items"]
        for item in items:
            ra_rom = RA_Rom(
                file_path=Path(item["path"]),
                label=item["label"],
                crc32=item["crc32"].split("|")[0],
                playlist_name=Path(item["db_name"]).name,
            )
            ra_rom_list.append(ra_rom)

    exist_rom_crc32_to_file_path_dict = {}
    new_roms_count = 0
    for ra_rom in ra_rom_list:
        if not fnmatch.fnmatch(
            ra_rom.file_path, f"*{WiiFlow_Configs.rom_file_extension()}"
        ):
            continue

        if RomsDB.rom_exist(ra_rom.crc32):
            exist_rom_crc32_to_file_path_dict[ra_rom.crc32] = ra_rom.file_path
            continue

        wiiflow_rom = WiiFlow_RomsDB.query_rom(
            rom_crc32=ra_rom.crc32, rom_file_title=ra_rom.file_path.stem
        )
        if wiiflow_rom is None:
            print(
                f"未知的 ROM 文件：{ra_rom.file_path.name} ra_rom.crc32={ra_rom.crc32}"
            )
            continue

        wiiflow_game = WiiFlow_GamesDB.query_game(game_id=wiiflow_rom.game_id)
        print(f'\t<Game id="{wiiflow_game.id}"')
        print(f'\t\ten_title="{wiiflow_game.en_title}"')
        print(f'\t\tzhcn_title="{wiiflow_game.zhcn_title}"')
        print('\t\thfsplay="" launchbox="">')

        rom_bytes = str(ra_rom.file_path.stat().st_size)
        print(f'\t\t<Rom crc32="{ra_rom.crc32}" bytes="{rom_bytes}"')
        print(f'\t\t\tfile_name="{ra_rom.file_path.name}"')
        print(f'\t\t\ten_title="{ra_rom.label}"')
        print('\t\t\tzhcn_title=""')
        print('\t\t\tcores-work="" cores-not-work=""')
        print("\t\t/>")
        print("\t</Game>")

        print(f"导入 ROM 文件：{ra_rom.file_path.name} ra_rom.crc32={ra_rom.crc32}")
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
            crc32=ra_rom.crc32,
            bytes=rom_bytes,
            file_name=ra_rom.file_path.name,
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
                print(
                    f"【错误】ROM 文件已经存在，但未在 .xml 文件中配置：{dst_rom_file_path}"
                )
                continue

        if Helper.verify_exist_directory_ex(dst_rom_file_path.parent):
            Helper.copy_file_if_not_exist(ra_rom.file_path, dst_rom_file_path)
            print(f"\t{ra_rom.file_path.name} -> {dst_rom_file_path}")
            new_roms_count = new_roms_count + 1

    if new_roms_count == 0:
        print("无新游戏导入")
    else:
        print(f"已导入 {new_roms_count} 个新游戏")

    exist_roms_count = len(exist_rom_crc32_to_file_path_dict)
    if exist_roms_count > 0:
        print(
            f"【提示】下列 .lpl 文件中 ROM 文件已经存在，无需导入（共 {exist_roms_count} 个）："
        )
        for rom_crc32, rom_file_path in exist_rom_crc32_to_file_path_dict.items():
            print(f"\t{rom_file_path} crc32={rom_crc32}")
