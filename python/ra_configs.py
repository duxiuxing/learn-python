# -- coding: UTF-8 --

from pathlib import Path


class RA_Configs:
    _db_name = None

    @staticmethod
    def db_name() -> Path:
        return RA_Configs._db_name

    _roms_relative_directory = None

    @staticmethod
    def roms_relative_directory() -> Path:
        return RA_Configs._roms_relative_directory
