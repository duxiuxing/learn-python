# -- coding: UTF-8 --

from local_configs import LocalConfigs
from pathlib import Path


class WiiSS_Configs:
    @staticmethod
    def template_cfg_file_name() -> Path:
        return Path(f"{WiiSS_Configs.core_file_name.stem}.cfg")

    core_file_name = None

    @staticmethod
    def repository_directory() -> Path:
        return LocalConfigs.repository_directory.joinpath("wii\\RA-HEXAECO")

    # private 文件夹里的数据文件夹名称
    data_folder_name = None

    # .dol 发布的年月日
    release_date = None

    settings_dict = {}
