# -- coding: UTF-8 --

import os
import shutil

from console_configs import ConsoleConfigs
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
    def compute_png_cover_file_path(rom: WiiFlow_Rom):
        game = WiiFlow_GamesDB.query_game(game_id=rom.game_id)
        repository_dir = Path(LocalConfigs.repository_directory())
        plugin_name = WiiFlow_Configs.plugin_name()

        if Helper.files_in_letter_folder():
            letter = game.name.upper()[0]
            if letter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                letter = "#"
            return repository_dir.joinpath(
                f"wii\\wiiflow\\boxcovers\\{plugin_name}\\{letter}\\{rom.file_title}{ConsoleConfigs.rom_file_extension()}.png",
            )
        else:
            return repository_dir.joinpath(
                f"wii\\wiiflow\\boxcovers\\{plugin_name}\\{rom.file_title}{ConsoleConfigs.rom_file_extension()}.png",
            )

    @staticmethod
    def compute_wfc_cover_file_path(rom: WiiFlow_Rom):
        game = WiiFlow_GamesDB.query_game(game_id=rom.game_id)
        repository_dir = Path(LocalConfigs.repository_directory())        
        plugin_name = WiiFlow_Configs.plugin_name()

        if Helper.files_in_letter_folder():
            letter = game.name.upper()[0]
            if letter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                letter = "#"
            return repository_dir.joinpath(
                f"wii\\wiiflow\\cache\\{plugin_name}\\{letter}\\{rom.file_title}{ConsoleConfigs.rom_file_extension()}.wfc",
            )
        else:
            return repository_dir.joinpath(
                f"wii\\wiiflow\\cache\\{plugin_name}\\{rom.file_title}{ConsoleConfigs.rom_file_extension()}.wfc",
            )
