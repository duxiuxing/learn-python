# -- coding: UTF-8 --

from helper import Helper
from local_configs import LocalConfigs
from pathlib import Path
from wiiflow_configs import WiiFlow_Configs
from wiiflow_game import WiiFlow_Game
from wiiflow_games_db import WiiFlow_GamesDB
from wiiflow_rom import WiiFlow_Rom
from wiiflow_roms_db import WiiFlow_RomsDB


class WiiFlow_ResourceFileHelper:
    @staticmethod
    def png_blank_cover_path():
        return LocalConfigs.repository_directory().joinpath(
            "wii\\wiiflow\\boxcovers\\blank_covers",
            f"{WiiFlow_Configs.plugin_name()}.png",
        )

    @staticmethod
    def png_cover_root_directory():
        return LocalConfigs.repository_directory().joinpath(
            f"wii\\wiiflow\\boxcovers\\{WiiFlow_Configs.plugin_name()}"
        )

    @staticmethod
    def compute_png_cover_path(rom_file_name):
        if Helper.files_in_letter_folder():
            rom = WiiFlow_RomsDB.query_rom(rom_file_title=Path(rom_file_name).stem)
            game = WiiFlow_GamesDB.query_game(game_id=rom.game_id)
            letter = game.name.upper()[0]
            if letter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                letter = "#"
            return LocalConfigs.repository_directory().joinpath(
                WiiFlow_ResourceFileHelper.png_cover_root_directory(),
                f"{letter}\\{rom_file_name}.png",
            )
        else:
            return LocalConfigs.repository_directory().joinpath(
                WiiFlow_ResourceFileHelper.png_cover_root_directory(),
                f"{rom_file_name}.png",
            )

    @staticmethod
    def wfc_blank_cover_path():
        return LocalConfigs.repository_directory().joinpath(
            "wii\\wiiflow\\cache\\blank_covers", f"{WiiFlow_Configs.plugin_name()}.wfc"
        )

    @staticmethod
    def compute_wfc_cover_path(rom_file_name):
        if Helper.files_in_letter_folder():
            rom = WiiFlow_RomsDB.query_rom(rom_file_title=Path(rom_file_name).stem)
            game = WiiFlow_GamesDB.query_game(game_id=rom.game_id)
            letter = game.name.upper()[0]
            if letter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                letter = "#"
            return LocalConfigs.repository_directory().joinpath(
                "wii\\wiiflow\\cache",
                f"{WiiFlow_Configs.plugin_name()}\\{letter}\\{rom_file_name}.wfc",
            )
        else:
            return LocalConfigs.repository_directory().joinpath(
                "wii\\wiiflow\\cache",
                f"{WiiFlow_Configs.plugin_name()}\\{rom_file_name}.wfc",
            )
