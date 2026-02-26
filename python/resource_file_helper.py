# -- coding: UTF-8 --

from game import Game
from games_db import GamesDB
from helper import Helper
from local_configs import LocalConfigs
from pathlib import Path
from rom import Rom
from roms_db import RomsDB


class ResourceFileHelper:
    @staticmethod
    def compute_rom_file_path(rom: Rom, include_crc32: bool) -> Path:
        """
        获得 rom 文件在库里面的文件路径

        Args:
            rom (Rom): rom 文件对应的 Rom 对象
            include_crc32 (bool): 路径中是否包含 crc32

        Returns:
            Path: rom 文件的路径
        """
        game = GamesDB.query_game(game_id=rom.game_id)
        repository_dir = LocalConfigs.repository_directory()

        rom_file_parent_dir = None
        if Helper.files_in_letter_folder():
            letter = game.en_title.upper()[0]
            if letter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                letter = "#"
            rom_file_parent_dir = repository_dir.joinpath(f"roms\\{letter}")
        else:
            rom_file_parent_dir = repository_dir.joinpath("roms")

        if include_crc32:
            return rom_file_parent_dir.joinpath(f"{rom.crc32}\\{rom.file_name}")
        else:
            return rom_file_parent_dir.joinpath(rom.file_name)

    @staticmethod
    def compute_rom_media_file_path(
        rom: Rom, folder_name: str, file_extension: str
    ) -> Path:
        """
        获得 rom 对应的媒体文件在库里面的文件路径

        Args:
            rom (Rom): rom 文件对应的 Rom 对象
            folder_name (str): 媒体文件所在的文件夹名称
            file_extension (str): 文件后缀名

        Returns:
            Path: 媒体文件的路径
        """
        game = GamesDB.get_game_by_id(rom.game_id)
        repository_dir = LocalConfigs.repository_directory()

        media_file_parent_dir = None
        if Helper.files_in_letter_folder():
            letter = game.en_title.upper()[0]
            if letter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                letter = "#"
            media_file_parent_dir = repository_dir.joinpath(
                f"media\\{folder_name}\\{letter}"
            )
        else:
            media_file_parent_dir = repository_dir.joinpath(f"media\\{folder_name}")

        return media_file_parent_dir.joinpath(f"{rom.file_name.stem}{file_extension}")

    @staticmethod
    def compute_game_media_file_path(
        game: Game, folder_name: str, file_extension: str
    ) -> Path:
        """
        获得游戏对应的媒体文件在库里面的文件路径

        Args:
            game (Game): 游戏对应的 Game 对象
            folder_name (str): 媒体文件所在的文件夹名称
            file_extension (str): 文件后缀名

        Returns:
            Path: 媒体文件的路径
        """
        repository_dir = LocalConfigs.repository_directory()

        media_file_parent_dir = None
        if Helper.files_in_letter_folder():
            letter = game.en_title.upper()[0]
            if letter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                letter = "#"
            media_file_parent_dir = repository_dir.joinpath(
                f"media\\{folder_name}\\{letter}"
            )
        else:
            media_file_parent_dir = repository_dir.joinpath(f"media\\{folder_name}")

        return media_file_parent_dir.joinpath(f"{game.en_title}{file_extension}")
