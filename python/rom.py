# -- coding: UTF-8 --

from pathlib import Path


class Rom:
    def __init__(self, file_name, crc32=None):
        self.file_name = Path(file_name)
        self.crc32 = crc32
        self.bytes = None
        self.game_id = None
        self.parent_rom = None
        self.en_title = None
        self.zhcn_title = None
