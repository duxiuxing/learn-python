# -- coding: UTF-8 --

from python.rom import Rom


class RomExportInfo(Rom):
    def __init__(self, rom_info):
        super().__init__(
            game_id=rom_info.game_name,
            crc32=rom_info.rom_crc32,
            bytes=rom_info.rom_bytes,
            file=rom_info.rom_title,
            en_title=rom_info.en_title,
            zhcn_title=rom_info.zhcn_title,
        )
        self.src_path = None
        self.dst_path = None
