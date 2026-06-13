# -- coding: UTF-8 --

from local_configs import LocalConfigs
from pathlib import Path
from ra_configs import RA_Configs


class RA_PlaylistConfigs:
    def __init__(self):
        self._head = None

        self.lpl_file_path = None
        self.item_list = []
        self.png_file_match_rom_file = False
        self.boxarts_folder = "boxart"
        self.logos_folder = "logo"
        self.snaps_folder = "snap"
        self.titles_folder = "title"
        self.roms_relative_directory = None

    def get_lpl_file_path(self):
        if self.lpl_file_path is None:
            return LocalConfigs.export_to_directory.joinpath(
                f"playlists\\{RA_Configs.lpl_file_name}",
            )
        else:
            return self.lpl_file_path

    def set_head(self, head):
        self._head = head

    def get_head(self):
        if self._head is None:
            return (
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
        else:
            return self._head
