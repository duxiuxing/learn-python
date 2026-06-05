# -- coding: UTF-8 --

from game import Game
from games_db import GamesDB
from helper import Helper
from local_configs import LocalConfigs
from pathlib import Path
from PIL import Image
from ra_configs import RA_Configs
from ra_playlist_config import LiteRom
from ra_playlist_config import RA_PlaylistConfig
from resource_file_helper import ResourceFileHelper
from rom import Rom
from roms_db import RomsDB


class RA_Playlist:
    def __init__(self, configs: RA_PlaylistConfig):
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
        dst_dir = LocalConfigs.export_to_directory().joinpath(
            RA_Configs.roms_relative_directory()
        )
        for rom in self.configs.rom_list:
            RA_Playlist.export_rom_file(rom, dst_dir)
            RA_Playlist.export_rom_file(rom.parent_rom, dst_dir)

    def export_lpl_file(self):
        lpl_file_path = LocalConfigs.export_to_directory().joinpath(
            f"playlists\\{RA_Configs.lpl_file_name()}",
        )
        if not Helper.verify_exist_directory_ex(lpl_file_path.parent):
            print(f"【错误】无效的目标文件 {lpl_file_path}")
            return
        if lpl_file_path.exists() and lpl_file_path.is_file():
            lpl_file_path.unlink()

        with open(lpl_file_path, "w", encoding="utf-8") as lpl_file:
            head = (
                "{\n"
                '  "version": "1.5",\n'
                '  "default_core_path": "DETECT",\n'
                '  "default_core_name": "DETECT",\n'
                '  "label_display_mode": 0,\n'
                '  "right_thumbnail_mode": 4,\n'
                '  "left_thumbnail_mode": 2,\n'
                '  "thumbnail_match_mode": 0,\n'
                '  "sort_mode": 1,\n'
                '  "items": [\n'
            )
            lpl_file.write(head)

            first_rom = True
            for rom in self.configs.rom_list:
                if first_rom:
                    first_rom = False
                    lpl_file.write("    {\n")
                else:
                    lpl_file.write(",\n    {\n")

                lpl_file.write(
                    f'      "path": "{self.configs.rom_path_prefix}{rom.file_name}",\n'
                )

                game = GamesDB.query_game(game_id=rom.game_id)
                label = game.en_title
                if self.configs.use_zhcn_title_as_label:
                    label = game.zhcn_title
                lpl_file.write(f'      "label": "{label}",\n')

                lpl_file.write('      "core_path": "DETECT",\n')
                lpl_file.write('      "core_name": "DETECT",\n')
                lpl_file.write(f'      "crc32": "{rom.crc32}|crc",\n')
                lpl_file.write(f'      "db_name": "{RA_Configs.lpl_file_name()}"\n')
                lpl_file.write("    }")

            lpl_file.write("\n  ]\n}\n")
            lpl_file.close()

    def export_thumbnails(self, src_folder_name, dst_folder_name):
        if src_folder_name is None:
            return

        dst_dir = LocalConfigs.export_to_directory().joinpath(
            f"thumbnails\\{RA_Configs.lpl_file_name().stem}\\{dst_folder_name}",
        )
        for rom in self.configs.rom_list:
            src_file_path = ResourceFileHelper.compute_rom_media_file_path(
                rom, src_folder_name, ".png"
            )
            dst_file_name = f"{rom.file_name.stem}.png"
            if not self.configs.png_file_match_rom_file:
                game = GamesDB.query_game(game_id=rom.game_id)
                label = game.en_title
                if self.configs.use_zhcn_title_as_label:
                    label = game.zhcn_title
                dst_file_name = f"{label}.png"
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
