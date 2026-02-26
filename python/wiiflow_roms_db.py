# -- coding: UTF-8 --

from wiiflow_rom import WiiFlow_Rom


class WiiFlow_RomsDB:
    __instance = None

    @staticmethod
    def _instance():
        if WiiFlow_RomsDB.__instance is None:
            WiiFlow_RomsDB()
        return WiiFlow_RomsDB.__instance

    def __init__(self):
        WiiFlow_RomsDB.__instance = self
        self._crc32_to_rom = {}

    @staticmethod
    def all_rom_crc32_values():
        return WiiFlow_RomsDB._instance()._crc32_to_rom.keys()

    @staticmethod
    def all_roms():
        return WiiFlow_RomsDB._instance()._crc32_to_rom.values()

    @staticmethod
    def rom_exist(rom_crc32):
        return rom_crc32 in WiiFlow_RomsDB._instance()._crc32_to_rom.keys()

    @staticmethod
    def add_rom(rom: WiiFlow_Rom):
        WiiFlow_RomsDB._instance()._crc32_to_rom[rom.crc32] = rom

    @staticmethod
    def query_rom(rom_crc32=None, rom_file_title=None):
        roms_db = WiiFlow_RomsDB._instance()
        if rom_crc32 is not None:
            return roms_db._crc32_to_rom.get(rom_crc32)

        if rom_file_title is not None:
            for rom in roms_db._crc32_to_rom.values():
                if rom.file_title == rom_file_title:
                    return rom

        return None
