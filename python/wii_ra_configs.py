# -- coding: UTF-8 --

from pathlib import Path


class WiiRA_Configs:
    _core_name = None

    @staticmethod
    def core_name() -> str:
        return WiiRA_Configs._core_name

    _core_file_name = None

    @staticmethod
    def core_file_name() -> Path:
        return WiiRA_Configs._core_file_name

    _core_info_file_name = None

    @staticmethod
    def core_info_file_name() -> Path:
        return WiiRA_Configs._core_info_file_name

    _db_name = None

    @staticmethod
    def db_name() -> Path:
        return WiiRA_Configs._db_name

    _release_date = None

    @staticmethod
    def release_date() -> str:
        return WiiRA_Configs._release_date

    _version = None

    @staticmethod
    def version() -> str:
        return WiiRA_Configs._version
