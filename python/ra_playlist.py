# -- coding: UTF-8 --

from game import Game
from games_db import GamesDB
from helper import Helper
from local_configs import LocalConfigs
from pathlib import Path
from PIL import Image
from ra_configs import RA_Configs
from ra_playlist_configs import RA_PlaylistConfigs
from ra_playlist_item import RA_PlaylistItem
from resource_file_helper import ResourceFileHelper
from rom import Rom
from roms_db import RomsDB


class RA_Playlist:
    def __init__(self, configs: RA_PlaylistConfigs):
        self.configs = configs

    @staticmethod
    def export_rom_file(rom: Rom, dst_dir: Path):
        if rom is None:
            return

        src_file_path = ResourceFileHelper.compute_rom_file_path(rom, True)
        if not src_file_path.exists():
            src_file_path = ResourceFileHelper.compute_rom_file_path(rom, False)

        if not src_file_path.exists():
            print(f"【错误】无效的源文件 {src_file_path}")
            return

        Helper.copy_file_to_directory(src_file_path, dst_dir)

    def export_rom_files(self):
        dst_dir = LocalConfigs.export_to_directory.joinpath(
            self.configs.roms_relative_directory
        )
        for item in self.configs.item_list:
            rom = RomsDB.query_rom(rom_crc32=item.crc32)
            RA_Playlist.export_rom_file(rom, dst_dir)
            RA_Playlist.export_rom_file(rom.parent_rom, dst_dir)

    def export_lpl_file(self):
        lpl_file_path = self.configs.get_lpl_file_path()
        if not Helper.verify_exist_directory_ex(lpl_file_path.parent):
            print(f"【错误】无效的目标文件 {lpl_file_path}")
            return
        if lpl_file_path.exists() and lpl_file_path.is_file():
            lpl_file_path.unlink()

        with open(lpl_file_path, "w", encoding="utf-8") as lpl_file:
            lpl_file.write(self.configs.get_head())

            first_item = True
            for item in self.configs.item_list:
                if first_item:
                    first_item = False
                    lpl_file.write("    {\n")
                else:
                    lpl_file.write(",\n    {\n")

                lpl_file.write(f'      "path": "{item.path}",\n')
                lpl_file.write(f'      "label": "{item.label}",\n')
                lpl_file.write('      "core_path": "DETECT",\n')
                lpl_file.write('      "core_name": "DETECT",\n')
                lpl_file.write(f'      "crc32": "{item.crc32}|crc",\n')
                lpl_file.write(f'      "db_name": "{item.db_name}"\n')
                lpl_file.write("    }")

            lpl_file.write("\n  ]\n}\n")
            lpl_file.close()

    def export_thumbnails(self, src_folder_name, dst_folder_name):
        if src_folder_name is None:
            return

        dst_dir = LocalConfigs.export_to_directory.joinpath(
            f"thumbnails\\{RA_Configs.lpl_file_name.stem}\\{dst_folder_name}",
        )
        for item in self.configs.item_list:
            rom = RomsDB.query_rom(rom_crc32=item.crc32)
            src_file_path = ResourceFileHelper.compute_rom_media_file_path(
                rom, src_folder_name, ".png"
            )
            dst_file_name = f"{rom.file_title()}.png"
            if not self.configs.png_file_match_rom_file:
                dst_file_name = f"{item.label}.png"
            dst_file_path = dst_dir.joinpath(dst_file_name)
            Helper.copy_file_if_not_exist(src_file_path, dst_file_path)

    def export_thumbnails_boxarts(self):
        self.export_thumbnails(self.configs.boxarts_folder, "Named_Boxarts")

    def export_thumbnails_logos(self):
        self.export_thumbnails(self.configs.logos_folder, "Named_Logos")

    def export_thumbnails_snaps(self):
        self.export_thumbnails(self.configs.snaps_folder, "Named_Snaps")

    def export_thumbnails_titles(self):
        self.export_thumbnails(self.configs.titles_folder, "Named_Titles")

    def export_all(self):
        self.export_rom_files()
        self.export_lpl_file()
        self.export_thumbnails_boxarts()
        self.export_thumbnails_logos()
        self.export_thumbnails_snaps()
        self.export_thumbnails_titles()
