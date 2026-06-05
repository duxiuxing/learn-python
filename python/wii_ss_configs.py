# -- coding: UTF-8 --

from pathlib import Path


class WiiSS_Configs:
    _core_cfg_template_file_name = None

    @staticmethod
    def core_cfg_template_file_name() -> Path:
        if WiiSS_Configs._core_cfg_template_file_name is None:
            return f"{WiiSS_Configs.core_file_name().stem}.cfg"
        else:
            return WiiSS_Configs._core_cfg_template_file_name

    _core_file_name = None

    @staticmethod
    def core_file_name() -> Path:
        return WiiSS_Configs._core_file_name

    _core_folder_name = "RA-HEXAECO"

    @staticmethod
    def core_folder_name() -> str:
        return WiiSS_Configs._core_folder_name

    _data_folder_name = None

    @staticmethod
    def data_folder_name() -> str:
        return WiiSS_Configs._data_folder_name

    _release_date = None

    @staticmethod
    def release_date() -> str:
        return WiiSS_Configs._release_date

    _system_directory = None

    @staticmethod
    def system_directory() -> str:
        return WiiSS_Configs._system_directory
