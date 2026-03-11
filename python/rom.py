# -- coding: UTF-8 --

from pathlib import Path


class Rom:
    def __init__(
        self,
        game_id,
        crc32,
        bytes,
        file_name,
        parent_rom,
        en_title,
        zhcn_title,
    ):
        self.game_id = game_id
        self.crc32 = crc32
        self.bytes = bytes
        self.file_name = Path(file_name)
        self.parent_rom = parent_rom
        self.en_title = en_title
        self.zhcn_title = zhcn_title
