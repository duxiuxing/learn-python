# -- coding: UTF-8 --

from rom import Rom


class RomsDB:
    __instance = None

    @staticmethod
    def _instance():
        if RomsDB.__instance is None:
            RomsDB()
        return RomsDB.__instance

    def __init__(self):
        RomsDB.__instance = self
        self._crc32_to_rom = {}

    @staticmethod
    def all_rom_crc32_values():
        return RomsDB._instance()._crc32_to_rom.keys()

    @staticmethod
    def all_roms():
        return RomsDB._instance()._crc32_to_rom.values()

    @staticmethod
    def rom_exist(rom_crc32):
        return rom_crc32 in RomsDB._instance()._crc32_to_rom.keys()

    @staticmethod
    def add_rom(rom: Rom):
        RomsDB._instance()._crc32_to_rom[rom.crc32] = rom

    @staticmethod
    def query_rom(rom_crc32=None, rom_file_name=None):
        roms_db = RomsDB._instance()
        if rom_crc32 is not None:
            return roms_db._crc32_to_rom.get(rom_crc32)

        if rom_file_name is not None:
            for rom in roms_db._crc32_to_rom.values():
                if rom.file_name == rom_file_name:
                    return rom

        return None
