# -- coding: UTF-8 --

from pathlib import Path


class WiiRA_Configs:
    _core_cfg_file_name = Path("retroarch.cfg")

    @staticmethod
    def core_cfg_file_name() -> Path:
        return WiiRA_Configs._core_cfg_file_name

    _core_name = None

    @staticmethod
    def core_name() -> str:
        return WiiRA_Configs._core_name

    _core_file_name = None

    @staticmethod
    def core_file_name() -> Path:
        return WiiRA_Configs._core_file_name

    _core_folder_name = "retroarch-wii"

    @staticmethod
    def core_folder_name() -> str:
        return WiiRA_Configs._core_folder_name

    _core_info_file_name = None

    @staticmethod
    def core_info_file_name() -> Path:
        return WiiRA_Configs._core_info_file_name

    _release_date = None

    @staticmethod
    def release_date() -> str:
        return WiiRA_Configs._release_date

    _version = None

    @staticmethod
    def version() -> str:
        return WiiRA_Configs._version

    _roms_relative_directory = None

    @staticmethod
    def roms_relative_directory() -> Path:
        return WiiRA_Configs._roms_relative_directory
