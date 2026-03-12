# -- coding: UTF-8 --

import fnmatch
import os
import re

from helper import Helper
from init_global_configs import Init_Global_Configs
from local_configs import LocalConfigs
from pathlib import Path
from resource_file_helper import ResourceFileHelper
from rom import Rom
from roms_db import RomsDB
from wii_ra_configs import WiiRA_Configs
from wiiflow_configs import WiiFlow_Configs
from wiiflow_game import WiiFlow_Game
from wiiflow_games_db import WiiFlow_GamesDB
from wiiflow_resource_file_helper import WiiFlow_ResourceFileHelper


def f1_2_export_png_covers(delete_dst_file_first: bool):
    # 先处理默认封面文件
    dst_dir = LocalConfigs.export_to_directory().joinpath(
        "wiiflow\\boxcovers\\blank_covers"
    )
    if not Helper.verify_exist_directory_ex(dst_dir):
        print(f"【错误】无效的目标文件夹 {dst_dir}")
        return
    src_file_path = WiiFlow_ResourceFileHelper.png_blank_cover_path()
    if src_file_path.exists():
        dst_file_path = dst_dir.joinpath(src_file_path.name)
        if delete_dst_file_first:
            if dst_file_path.exists() and dst_file_path.is_file():
                dst_file_path.unlink()
        Helper.copy_file_to_directory(src_file_path, dst_dir)
    else:
        print(f"【错误】无效的源文件 {src_file_path}")

    # 再处理其他封面文件
    roms_dir = LocalConfigs.export_to_directory().joinpath(
        WiiRA_Configs.roms_directory()
    )
    if not roms_dir.exists():
        print(f"【错误】无效的 ROM 文件夹路径：{roms_dir}")
        return

    plugin_name = WiiFlow_Configs.plugin_name()
    dst_dir = LocalConfigs.export_to_directory().joinpath(
        f"wiiflow\\boxcovers\\{plugin_name}"
    )
    if not Helper.verify_exist_directory_ex(dst_dir):
        print(f"【错误】无效的目标文件夹 {dst_dir}")
        return

    print(
        f"\nROM 文件夹：{roms_dir}\n"
        "程序会根据 ROM 文件夹里的文件，把对应的 .png 格式的封面文件导出到目标文件夹\n"
        f"目标文件夹：{dst_dir}"
    )

    rom_file_count = 0
    for rom_file_name in os.listdir(roms_dir):
        if not WiiFlow_Configs.is_rom_file_name(rom_file_name):
            continue
        rom_file_count = rom_file_count + 1
        src_file_path = WiiFlow_ResourceFileHelper.compute_png_cover_path(rom_file_name)
        if not src_file_path.exists():
            print(f"【错误】无效的源文件 {src_file_path}")
            continue
        dst_file_path = dst_dir.joinpath(src_file_path.name)
        if delete_dst_file_first:
            if dst_file_path.exists() and dst_file_path.is_file():
                dst_file_path.unlink()
        Helper.copy_file_to_directory(src_file_path, dst_dir)

    cover_file_count = 0
    for cover_file_name in os.listdir(dst_dir):
        if not fnmatch.fnmatch(cover_file_name, "*.png"):
            continue
        cover_file_count = cover_file_count + 1

    print(f"导出完毕，ROM 文件数：{rom_file_count}，封面文件数：{cover_file_count}")


def f3_4_export_wfc_covers(delete_dst_file_first: bool):
    # 先处理默认封面文件
    dst_dir = LocalConfigs.export_to_directory().joinpath(
        "wiiflow\\cache\\blank_covers"
    )
    if not Helper.verify_exist_directory_ex(dst_dir):
        print(f"【错误】无效的目标文件夹 {dst_dir}")
        return
    src_file_path = WiiFlow_ResourceFileHelper.wfc_blank_cover_path()
    if src_file_path.exists():
        dst_file_path = dst_dir.joinpath(src_file_path.name)
        if delete_dst_file_first:
            if dst_file_path.exists() and dst_file_path.is_file():
                dst_file_path.unlink()
        Helper.copy_file_to_directory(src_file_path, dst_dir)
    else:
        print(f"【错误】无效的源文件 {src_file_path}")

    # 再处理其他封面文件
    roms_dir = LocalConfigs.export_to_directory().joinpath(
        WiiRA_Configs.roms_directory()
    )
    if not roms_dir.exists():
        print(f"【错误】无效的 ROM 文件夹路径：{roms_dir}")
        return

    plugin_name = WiiFlow_Configs.plugin_name()
    dst_dir = LocalConfigs.export_to_directory().joinpath(
        f"wiiflow\\cache\\{plugin_name}"
    )
    if not Helper.verify_exist_directory_ex(dst_dir):
        print(f"【错误】无效的目标文件夹 {dst_dir}")
        return

    print(
        f"\nROM 文件夹：{roms_dir}\n"
        "程序会根据 ROM 文件夹里的文件，把对应的 .wfc 格式的封面文件导出到目标文件夹\n"
        f"目标文件夹：{dst_dir}"
    )

    rom_file_count = 0
    for rom_file_name in os.listdir(roms_dir):
        if not WiiFlow_Configs.is_rom_file_name(rom_file_name):
            continue
        rom_file_count = rom_file_count + 1
        src_file_path = WiiFlow_ResourceFileHelper.compute_wfc_cover_path(rom_file_name)
        if not src_file_path.exists():
            print(f"【错误】无效的源文件 {src_file_path}")
            continue
        dst_file_path = dst_dir.joinpath(src_file_path.name)
        if delete_dst_file_first:
            if dst_file_path.exists() and dst_file_path.is_file():
                dst_file_path.unlink()
        Helper.copy_file_to_directory(src_file_path, dst_dir)

    cover_file_count = 0
    for cover_file_name in os.listdir(dst_dir):
        if not fnmatch.fnmatch(cover_file_name, "*.wfc"):
            continue
        cover_file_count = cover_file_count + 1

    print(f"导出完毕，ROM 文件数：{rom_file_count}，封面文件数：{cover_file_count}")


def f5_6_export_snapshots_by_rom_file_title(delete_dst_file_first: bool):
    roms_dir = LocalConfigs.export_to_directory().joinpath(
        WiiRA_Configs.roms_directory()
    )
    if not roms_dir.exists():
        print(f"【错误】无效的 ROM 文件夹路径：{roms_dir}")
        return

    plugin_name = WiiFlow_Configs.plugin_name()
    dst_dir = LocalConfigs.export_to_directory().joinpath(
        f"wiiflow\\snapshots\\{plugin_name}"
    )
    if not Helper.verify_exist_directory_ex(dst_dir):
        print(f"【错误】无效的目标文件夹 {dst_dir}")
        return

    print(
        f"\nROM 文件夹：{roms_dir}\n"
        "程序会根据 ROM 文件夹里的文件，把对应的截屏文件导出到目标文件夹\n"
        f"目标文件夹：{dst_dir}"
    )

    rom_file_count = 0
    for rom_file_name in os.listdir(roms_dir):
        if not WiiFlow_Configs.is_rom_file_name(rom_file_name):
            continue

        rom = RomsDB.query_rom(rom_file_name=rom_file_name)
        if rom is None:
            print(f"【提示】未知的 ROM 文件：{rom_file_name}")
            continue

        rom_file_count = rom_file_count + 1
        src_file_path = ResourceFileHelper.compute_rom_media_file_path(
            rom=rom, folder_name="snap", file_extension=".png"
        )
        if not src_file_path.exists():
            print(f"【错误】无效的源文件 {src_file_path}")
            continue
        dst_file_path = dst_dir.joinpath(f"{Path(rom_file_name).stem}.png")
        if delete_dst_file_first:
            if dst_file_path.exists() and dst_file_path.is_file():
                dst_file_path.unlink()
        Helper.copy_file_if_not_exist(src_file_path, dst_file_path)

    snap_file_count = 0
    for snap_file_name in os.listdir(dst_dir):
        if not fnmatch.fnmatch(snap_file_name, "*.png"):
            continue
        snap_file_count = snap_file_count + 1

    print(f"导出完毕，ROM 文件数：{rom_file_count}，截屏文件数：{snap_file_count}")


def f7_8_export_snapshots_by_game_name(delete_dst_file_first: bool):
    roms_dir = LocalConfigs.export_to_directory().joinpath(
        WiiRA_Configs.roms_directory()
    )
    if not roms_dir.exists():
        print(f"【错误】无效的 ROM 文件夹路径：{roms_dir}")
        return

    plugin_name = WiiFlow_Configs.plugin_name()
    dst_dir = LocalConfigs.export_to_directory().joinpath(
        f"wiiflow\\snapshots\\{plugin_name}"
    )
    if not Helper.verify_exist_directory_ex(dst_dir):
        print(f"【错误】无效的目标文件夹 {dst_dir}")
        return

    print(
        f"\nROM 文件夹：{roms_dir}\n"
        "程序会根据 ROM 文件夹里的文件，把对应的截屏文件导出到目标文件夹\n"
        f"目标文件夹：{dst_dir}"
    )

    rom_file_count = 0
    for rom_file_name in os.listdir(roms_dir):
        if not WiiFlow_Configs.is_rom_file_name(rom_file_name):
            continue

        rom = RomsDB.query_rom(rom_file_name=rom_file_name)
        if rom is None:
            print(f"【提示】未知的 ROM 文件：{rom_file_name}")
            continue

        rom_file_count = rom_file_count + 1
        src_file_path = ResourceFileHelper.compute_rom_media_file_path(
            rom=rom, folder_name="snap", file_extension=".png"
        )
        if not src_file_path.exists():
            print(f"【错误】无效的源文件 {src_file_path}")
            continue

        game = WiiFlow_GamesDB.query_game(game_id=rom.game_id)
        if game is None:
            print(
                f"【错误】未在 plugins_data 的 .xml 文件中配置：{rom_file_name} id={rom.game_id}"
            )
            continue

        dst_file_path = dst_dir.joinpath(f"{game.name}.png")
        if delete_dst_file_first:
            if dst_file_path.exists() and dst_file_path.is_file():
                dst_file_path.unlink()
        Helper.copy_file_if_not_exist(src_file_path, dst_file_path)

    snap_file_count = 0
    for snap_file_name in os.listdir(dst_dir):
        if not fnmatch.fnmatch(snap_file_name, "*.png"):
            continue
        snap_file_count = snap_file_count + 1

    print(f"导出完毕，ROM 文件数：{rom_file_count}，截屏文件数：{snap_file_count}")


def f9_export_plugin_files():
    src_dir = LocalConfigs.repository_directory().joinpath("wii\\wiiflow\\plugins")
    dst_dir = LocalConfigs.export_to_directory().joinpath("wiiflow\\plugins")
    Helper.copy_directory(src_dir, dst_dir)

    plugin_name = WiiFlow_Configs.plugin_name()
    dst_dir = LocalConfigs.export_to_directory().joinpath(
        f"wiiflow\\plugins_data\\{plugin_name}"
    )
    if not Helper.verify_exist_directory_ex(dst_dir):
        print(f"【错误】无效的目标文件夹 {dst_dir}")
        return

    file_name_list = [f"{plugin_name}.ini", f"{plugin_name}.xml"]
    for file_name in file_name_list:
        src_file_path = LocalConfigs.repository_directory().joinpath(
            f"wii\\wiiflow\\plugins_data\\{plugin_name}", file_name
        )
        dst_file_path = dst_dir.joinpath(file_name)
        if dst_file_path.exists() and dst_file_path.is_file():
            dst_file_path.unlink()
        Helper.copy_file_if_not_exist(src_file_path, dst_file_path)
        print(f"{file_name} -> {dst_file_path}")


if __name__ == "__main__":
    Init_Global_Configs()

    while True:
        export_to_dir = LocalConfigs.export_to_directory()
        print(
            f"\n即将导出 WiiFlow 文件到目标文件夹\n默认目标文件夹路径：{export_to_dir}"
        )
        user_input = input("请确认目标文件夹路径，使用默认路径请直接按回车 > ")
        if len(user_input) > 0:
            export_to_dir = Path(user_input)

        if export_to_dir.exists() and export_to_dir.is_dir():
            LocalConfigs._export_to_directory = export_to_dir
        else:
            print(f"【错误】无效的文件夹路径：{export_to_dir}")
            continue

        print(
            "\n1. 导出“所有”的 .png 格式的封面文件\n"
            "2. 仅导出“缺失”的 .png 格式的封面文件\n"
            "3. 导出“所有”的 .wfc 格式的封面文件\n"
            "4. 仅导出“缺失”的 .wfc 格式的封面文件\n"
            "5. 导出“所有”的截屏文件（以 ROM 文件命名）\n"
            "6. 仅导出“缺失”的截屏文件（以 ROM 文件命名）\n"
            "7. 导出“所有”的截屏文件（以游戏命名）\n"
            "8. 仅导出“缺失”的截屏文件（以游戏命名）\n"
            "9. 导出插件文件\n"
            "其他输入表示重新设置文件夹路径"
        )
        user_input = input("请输入操作的序号 > ")
        try:
            number = int(user_input)
            if number == 1:
                f1_2_export_png_covers(True)
            elif number == 2:
                f1_2_export_png_covers(False)
            elif number == 3:
                f3_4_export_wfc_covers(True)
            elif number == 4:
                f3_4_export_wfc_covers(False)
            elif number == 5:
                f5_6_export_snapshots_by_rom_file_title(True)
            elif number == 6:
                f5_6_export_snapshots_by_rom_file_title(False)
            elif number == 7:
                f7_8_export_snapshots_by_game_name(True)
            elif number == 8:
                f7_8_export_snapshots_by_game_name(False)
            elif number == 9:
                f9_export_plugin_files()
        except ValueError:
            continue
