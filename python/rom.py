# -- coding: UTF-8 --

from pathlib import Path


class Rom:
    def __init__(self, file_name: str, crc32: str | None = None):
        self.file_name = file_name
        self.crc32 = crc32
        self.bytes = None
        self.game_id = None
        self.parent_rom = None
        self.en_title = None
        self.zhcn_title = None

    def file_title(self):
        return Path(self.file_name).stem
