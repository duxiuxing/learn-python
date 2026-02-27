# -- coding: UTF-8 --

import json
import os

from init_global_configs import Init_Global_Configs
from local_configs import LocalConfigs
from pathlib import Path
from wii_ra_configs import WiiRA_Configs
from wiiflow_game import WiiFlow_Game
from wiiflow_games_db import WiiFlow_GamesDB
from wiiflow_rom import WiiFlow_Rom
from wiiflow_roms_db import WiiFlow_RomsDB


class RA_RenameThumbnails:
    @staticmethod
    def lpl_file_path():
        return LocalConfigs.retroarch_directory().joinpath(
            "playlists", WiiRA_Configs.db_name()
        )

    @staticmethod
    def thumbnails_directory():
        return LocalConfigs.retroarch_directory().joinpath(
            "thumbnails", WiiRA_Configs.db_name().stem
        )

    @staticmethod
    def rom_file_title_to_game_zhcn_title():
        # sf2ce.png -> 街头霸王2 冠军版.png
        thumbnails_dir = RA_RenameThumbnails.thumbnails_directory()
        with open(RA_RenameThumbnails.lpl_file_path(), "r", encoding="utf-8") as file:
            items = json.load(file)["items"]
            for item in items:
                rom_file_title = Path(item["path"]).stem
                rom = WiiFlow_RomsDB.query_rom(rom_file_title=rom_file_title)
                game = WiiFlow_GamesDB.query_game(game_id=rom.game_id)

                folder_names = [
                    "Named_Boxarts",
                    "Named_Logos",
                    "Named_Snaps",
                    "Named_Titles",
                ]
                for folder_name in folder_names:
                    folder_path = thumbnails_dir.joinpath(folder_name)
                    if folder_path.exists() and folder_path.is_dir():
                        old_file_path = folder_path.joinpath(f"{rom_file_title}.png")
                        new_file_path = folder_path.joinpath(f"{game.zhcn_title}.png")
                        if old_file_path.exists() and old_file_path.is_file():
                            os.rename(old_file_path, new_file_path)
                        elif not new_file_path.exists():
                            print(f"【错误】无效的源文件 {old_file_path}")

    @staticmethod
    def game_en_title_to_rom_file_title():
        # Street Fighter II' - Champion Edition.png -> sf2ce.png
        thumbnails_dir = RA_RenameThumbnails.thumbnails_directory()
        with open(RA_RenameThumbnails.lpl_file_path(), "r", encoding="utf-8") as file:
            items = json.load(file)["items"]
            for item in items:
                rom_file_title = Path(item["path"]).stem
                rom = WiiFlow_RomsDB.query_rom(rom_file_title=rom_file_title)
                game = WiiFlow_GamesDB.query_game(game_id=rom.game_id)

                folder_names = [
                    "Named_Boxarts",
                    "Named_Logos",
                    "Named_Snaps",
                    "Named_Titles",
                ]
                for folder_name in folder_names:
                    folder_path = thumbnails_dir.joinpath(folder_name)
                    if folder_path.exists() and folder_path.is_dir():
                        old_file_path = folder_path.joinpath(f"{game.en_title}.png")
                        new_file_path = folder_path.joinpath(f"{rom_file_title}.png")
                        if old_file_path.exists() and old_file_path.is_file():
                            os.rename(old_file_path, new_file_path)
                        elif not new_file_path.exists():
                            print(f"【错误】无效的源文件 {old_file_path}")

    @staticmethod
    def rom_file_title_to_label():
        # sf2ce.png -> J - 街头霸王2 冠军版.png
        thumbnails_dir = RA_RenameThumbnails.thumbnails_directory()
        with open(RA_RenameThumbnails.lpl_file_path(), "r", encoding="utf-8") as file:
            items = json.load(file)["items"]
            for item in items:
                rom_file_title = Path(item["path"]).stem
                label = item["label"]

                folder_names = [
                    "Named_Boxarts",
                    "Named_Logos",
                    "Named_Snaps",
                    "Named_Titles",
                ]
                for folder_name in folder_names:
                    folder_path = thumbnails_dir.joinpath(folder_name)
                    if folder_path.exists() and folder_path.is_dir():
                        old_file_path = folder_path.joinpath(f"{rom_file_title}.png")
                        new_file_path = folder_path.joinpath(f"{label}.png")
                        if old_file_path.exists() and old_file_path.is_file():
                            os.rename(old_file_path, new_file_path)
                        elif not new_file_path.exists():
                            print(f"【错误】无效的源文件 {old_file_path}")

    @staticmethod
    def label_to_rom_file_title():
        # J - 街头霸王2 冠军版.png -> sf2ce.png
        thumbnails_dir = RA_RenameThumbnails.thumbnails_directory()
        with open(RA_RenameThumbnails.lpl_file_path(), "r", encoding="utf-8") as file:
            items = json.load(file)["items"]
            for item in items:
                rom_file_title = Path(item["path"]).stem
                original_label = item["label"]
                label = original_label.replace(":", "_")
                label = original_label.replace("/", "_")

                folder_names = [
                    "Named_Boxarts",
                    "Named_Logos",
                    "Named_Snaps",
                    "Named_Titles",
                ]
                for folder_name in folder_names:
                    folder_path = thumbnails_dir.joinpath(folder_name)
                    if folder_path.exists() and folder_path.is_dir():
                        old_file_path = folder_path.joinpath(f"{label}.png")
                        new_file_path = folder_path.joinpath(f"{rom_file_title}.png")
                        if old_file_path.exists() and old_file_path.is_file():
                            os.rename(old_file_path, new_file_path)
                        elif not new_file_path.exists():
                            print(f"【错误】无效的源文件 {old_file_path}")


if __name__ == "__main__":
    Init_Global_Configs()

    # RA_RenameThumbnails.rom_file_title_to_label()
    # RA_RenameThumbnails.label_to_rom_file_title()
    # RA_RenameThumbnails.rom_file_title_to_game_en_title()
    RA_RenameThumbnails.game_en_title_to_rom_file_title()
