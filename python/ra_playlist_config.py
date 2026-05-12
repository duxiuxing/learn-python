# -- coding: UTF-8 --

from pathlib import Path
from rom import Rom
from roms_db import RomsDB


class LiteRom:
    def __init__(
        self,
        file_name,
        crc32=None,
    ):
        self.file_name = Path(file_name)
        self.crc32 = crc32


class RA_PlaylistConfig:
    def __init__(self, lite_rom_list: list):
        self.rom_list = []
        for lite_rom in lite_rom_list:
            self.rom_list.append(
                RomsDB.query_rom(
                    rom_crc32=lite_rom.crc32, rom_file_name=lite_rom.file_name
                )
            )
        self.rom_path_prefix = None
        self.use_zhcn_title_as_label = False
        self.png_file_match_rom_file = False

        self.boxarts_folder = "boxart"
        self.logos_folder = "logo"
        self.snaps_folder = "snap"
        self.titles_folder = "title"
