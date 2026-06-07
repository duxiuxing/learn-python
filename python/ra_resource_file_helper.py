# -- coding: UTF-8 --

from helper import Helper
from local_configs import LocalConfigs
from pathlib import Path
from ra_rom import RA_Rom


class RA_ResourceFileHelper:
    @staticmethod
    def playlist_png_directory():
        return LocalConfigs.retroarch_directory.joinpath(
            "assets\\xmb\\monochrome\\png"
        )

    @staticmethod
    def compute_game_media_file_path(
        ra_rom: RA_Rom, folder_name: str, file_extension: str
    ):
        file_title = ra_rom.label
        file_title = file_title.replace(":", "_")

        return LocalConfigs.retroarch_directory.joinpath(
            f"thumbnails\\{ra_rom.playlist_name.stem}\\{folder_name}\\{file_title}{file_extension}"
        )
