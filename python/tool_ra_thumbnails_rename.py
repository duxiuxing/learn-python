# -- coding: UTF-8 --

import json
import os
import time

from game import Game
from games_db import GamesDB
from init_global_configs import Init_Global_Configs
from local_configs import LocalConfigs
from pathlib import Path
from rom import Rom
from roms_db import RomsDB
from wii_ra_configs import WiiRA_Configs
from wiiflow_rom import WiiFlow_Rom
from wiiflow_roms_db import WiiFlow_RomsDB


class RA_ThumbnailsRename:
    @staticmethod
    def rename_file(old_file_path: Path, new_file_name):
        old_file_name = old_file_path.name
        if old_file_name.casefold() == new_file_name.casefold():
            temp_file_name = f"temp-{new_file_name}"
            old_file_path = RA_ThumbnailsRename.rename_file(
                old_file_path, temp_file_name
            )
            time.sleep(2)
            return RA_ThumbnailsRename.rename_file(old_file_path, new_file_name)
        else:
            new_file_path = old_file_path.parent.joinpath(new_file_name)
            if old_file_path.exists() and old_file_path.is_file():
                os.rename(old_file_path, new_file_path)
                return new_file_path
            else:
                print(f"【错误】无效的源文件 {old_file_path}")
                return None

    @staticmethod
    def default_lpl_file_path():
        return LocalConfigs.retroarch_directory().joinpath(
            "playlists", WiiRA_Configs.db_name()
        )

    @staticmethod
    def default_thumbnails_directory():
        return LocalConfigs.retroarch_directory().joinpath(
            "thumbnails", WiiRA_Configs.db_name().stem
        )

    @staticmethod
    def f3_rom_file_title_to_game_en_title(lpl_file_path: Path, png_folder_path: Path):
        # 3wonders.png -> Three Wonders.png
        if not png_folder_path.exists() or not png_folder_path.is_dir():
            print(f"【错误】无效的文件夹 {png_folder_path}")
            return

        with open(lpl_file_path, "r", encoding="utf-8") as file:
            items = json.load(file)["items"]
            for item in items:
                rom_file_name = Path(item["path"]).name
                rom_file_title = Path(rom_file_name).stem
                rom = RomsDB.query_rom(rom_file_name=rom_file_name)
                if rom is None:
                    rom = WiiFlow_RomsDB.query_rom(rom_file_title=rom_file_title)
                game = GamesDB.query_game(game_id=rom.game_id)

                print(f"{rom_file_title}.png -> {game.en_title}.png")
                old_file_path = png_folder_path.joinpath(f"{rom_file_title}.png")
                RA_ThumbnailsRename.rename_file(old_file_path, f"{game.en_title}.png")

    @staticmethod
    def f4_game_en_title_to_rom_file_title(lpl_file_path: Path, png_folder_path: Path):
        # Three Wonders.png -> 3wonders.png
        if not png_folder_path.exists() or not png_folder_path.is_dir():
            print(f"【错误】无效的文件夹 {png_folder_path}")
            return

        with open(lpl_file_path, "r", encoding="utf-8") as file:
            items = json.load(file)["items"]
            for item in items:
                rom_file_name = Path(item["path"]).name
                rom_file_title = Path(rom_file_name).stem
                rom = RomsDB.query_rom(rom_file_name=rom_file_name)
                if rom is None:
                    rom = WiiFlow_RomsDB.query_rom(
                        rom_file_title=Path(rom_file_name).stem
                    )
                game = GamesDB.query_game(game_id=rom.game_id)

                print(f"{game.en_title}.png -> {rom_file_title}.png")
                old_file_path = png_folder_path.joinpath(f"{game.en_title}.png")
                RA_ThumbnailsRename.rename_file(old_file_path, f"{rom_file_title}.png")

    @staticmethod
    def f2_rom_file_title_to_label(lpl_file_path: Path, png_folder_path: Path):
        # 3wonders.png -> label
        if not png_folder_path.exists() or not png_folder_path.is_dir():
            print(f"【错误】无效的文件夹 {png_folder_path}")
            return

        with open(lpl_file_path, "r", encoding="utf-8") as file:
            items = json.load(file)["items"]
            for item in items:
                rom_file_title = Path(item["path"]).stem
                original_label = item["label"]
                label = original_label.replace(":", "_").replace("/", "_")

                print(f"{rom_file_title}.png -> {label}.png")
                old_file_path = png_folder_path.joinpath(f"{rom_file_title}.png")
                RA_ThumbnailsRename.rename_file(old_file_path, f"{label}.png")

    @staticmethod
    def f1_label_to_rom_file_title(lpl_file_path: Path, png_folder_path: Path):
        # label -> 3wonders.png
        if not png_folder_path.exists() or not png_folder_path.is_dir():
            print(f"【错误】无效的文件夹 {png_folder_path}")
            return

        with open(lpl_file_path, "r", encoding="utf-8") as file:
            items = json.load(file)["items"]
            for item in items:
                rom_file_title = Path(item["path"]).stem
                original_label = item["label"]
                label = original_label.replace(":", "_").replace("/", "_")

                print(f"{label}.png -> {rom_file_title}.png")
                old_file_path = png_folder_path.joinpath(f"{label}.png")
                RA_ThumbnailsRename.rename_file(old_file_path, f"{rom_file_title}.png")

    @staticmethod
    def f5_label_to_game_en_title(lpl_file_path: Path, png_folder_path: Path):
        RA_ThumbnailsRename.f1_label_to_rom_file_title(
            lpl_file_path=lpl_file_path, png_folder_path=png_folder_path
        )
        RA_ThumbnailsRename.f3_rom_file_title_to_game_en_title(
            lpl_file_path=lpl_file_path, png_folder_path=png_folder_path
        )


if __name__ == "__main__":
    Init_Global_Configs()

    lpl_file_path = None
    while True:
        lpl_file_path = RA_ThumbnailsRename.default_lpl_file_path()
        print("\n即将根据 .lpl 文件对缩略图文件进行重命名")
        print(f"默认 .lpl 文件路径：{lpl_file_path}")
        user_input = input("请输入 .lpl 文件路径，使用默认路径请直接按回车 > ")
        if len(user_input) > 0:
            lpl_file_path = Path(user_input)

        if lpl_file_path.exists() and lpl_file_path.is_file():
            break
        else:
            print(f"【错误】无效的文件路径：{lpl_file_path}")

    thumbnails_dir = RA_ThumbnailsRename.default_thumbnails_directory()
    png_folder_path = None
    while True:
        print(
            "\n以下是预设的文件夹路径：\n"
            f"1.{thumbnails_dir.joinpath('Named_Boxarts')}\n"
            f"2.{thumbnails_dir.joinpath('Named_Logos')}\n"
            f"3.{thumbnails_dir.joinpath('Named_Snaps')}\n"
            f"4.{thumbnails_dir.joinpath('Named_Titles')}"
        )
        user_input = input(
            "请输入预设文件夹的序号或者自定义的文件夹路径（退出请直接按回车）\n> "
        )
        try:
            number = int(user_input)
            if number == 1:
                png_folder_path = thumbnails_dir.joinpath("Named_Boxarts")
            elif number == 2:
                png_folder_path = thumbnails_dir.joinpath("Named_Logos")
            elif number == 3:
                png_folder_path = thumbnails_dir.joinpath("Named_Snaps")
            elif number == 4:
                png_folder_path = thumbnails_dir.joinpath("Named_Titles")
            else:
                continue
        except ValueError:
            if len(user_input) > 0:
                folder_path = Path(user_input)
                if not folder_path.exists() or not folder_path.is_dir():
                    print(f"【错误】无效的文件夹路径：{folder_path}")
                    continue
                else:
                    png_folder_path = folder_path
            else:
                exit()

        print(
            "\n1. label -> 3wonders.png\n"
            "2. 3wonders.png -> label\n"
            "3. 3wonders.png -> Three Wonders.png\n"
            "4. Three Wonders.png -> 3wonders.png\n"
            "5. label -> Three Wonders.png\n"
            "其他输入表示重新设置文件夹路径"
        )
        user_input = input("请输入操作的序号 > ")
        try:
            number = int(user_input)
            if number == 1:
                RA_ThumbnailsRename.f1_label_to_rom_file_title(
                    lpl_file_path, png_folder_path
                )
            elif number == 2:
                RA_ThumbnailsRename.f2_rom_file_title_to_label(
                    lpl_file_path, png_folder_path
                )
            elif number == 3:
                RA_ThumbnailsRename.f3_rom_file_title_to_game_en_title(
                    lpl_file_path, png_folder_path
                )
            elif number == 4:
                RA_ThumbnailsRename.f4_game_en_title_to_rom_file_title(
                    lpl_file_path, png_folder_path
                )
            elif number == 5:
                RA_ThumbnailsRename.f5_label_to_game_en_title(
                    lpl_file_path, png_folder_path
                )
        except ValueError:
            continue
