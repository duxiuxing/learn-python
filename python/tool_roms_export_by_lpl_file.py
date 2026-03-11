# -- coding: UTF-8 --

import fnmatch
import json
import os

from helper import Helper
from init_global_configs import Init_Global_Configs
from local_configs import LocalConfigs
from pathlib import Path
from ra_rom import RA_Rom
from resource_file_helper import ResourceFileHelper
from rom import Rom
from roms_db import RomsDB
from wii_ra_configs import WiiRA_Configs
from wiiflow_configs import WiiFlow_Configs


if __name__ == "__main__":
    Init_Global_Configs()

    lpl_file_path = None
    while True:
        lpl_file_path = LocalConfigs.retroarch_directory().joinpath(
            "playlists", WiiRA_Configs.db_name()
        )
        print("\n即将根据 .lpl 文件导出 ROM 文件")
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

    while True:
        export_to_dir = LocalConfigs.export_to_directory()
        print(f"\n即将导出 ROM 文件到目标文件夹\n默认目标文件夹路径：{export_to_dir}")
        user_input = input("请确认目标文件夹路径，使用默认路径请直接按回车 > ")
        if len(user_input) > 0:
            export_to_dir = Path(user_input)

        if export_to_dir.exists() and export_to_dir.is_dir():
            LocalConfigs._export_to_directory = export_to_dir
        else:
            print(f"【错误】无效的文件夹路径：{export_to_dir}")
            continue

        dst_roms_dir = LocalConfigs.export_to_directory().joinpath(
            WiiRA_Configs.roms_directory()
        )
        if not Helper.verify_exist_directory_ex(dst_roms_dir):
            print(f"【错误】无效的文件夹路径：{dst_roms_dir}")
            continue

        not_exist_rom_crc32_to_file_path_dict = {}
        exist_roms_count = 0
        for ra_rom in ra_rom_list:
            if not fnmatch.fnmatch(
                ra_rom.file_path, f"*{WiiFlow_Configs.rom_file_extension()}"
            ):
                continue

            rom = RomsDB.query_rom(rom_crc32=ra_rom.crc32)
            if rom is None:
                not_exist_rom_crc32_to_file_path_dict[ra_rom.crc32] = ra_rom.file_path
                continue

            src_rom_file_path = ResourceFileHelper.compute_rom_file_path(
                rom=rom, include_crc32=True
            )
            if not src_rom_file_path.exists():
                src_rom_file_path = ResourceFileHelper.compute_rom_file_path(
                    rom=rom, include_crc32=False
                )

            if not src_rom_file_path.exists():
                print(
                    f"【错误】.xml 文件中的 ROM 文件并不存在：{rom.file_name} crc32={rom.crc32}"
                )
                continue

            Helper.copy_file_to_directory(src_rom_file_path, dst_roms_dir)
            exist_roms_count = exist_roms_count + 1

        if exist_roms_count == 0:
            print("无游戏导出")
        else:
            print(f"导出 {exist_roms_count} 个游戏")

        not_exist_roms_count = len(not_exist_rom_crc32_to_file_path_dict)
        if not_exist_roms_count > 0:
            print(
                f"【提示】下列 .lpl 文件中 ROM 文件不存在（共 {not_exist_roms_count} 个）："
            )
            for (
                rom_crc32,
                rom_file_path,
            ) in not_exist_rom_crc32_to_file_path_dict.items():
                print(f"\t{rom_file_path} crc32={rom_crc32}")
