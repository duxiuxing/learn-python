# -- coding: UTF-8 --

from local_configs import LocalConfigs
from pathlib import Path


class WiiSS_Configs:
    template_cfg_file_name = None

    @staticmethod
    def core_cfg_template_file_name() -> Path:
        if WiiSS_Configs.template_cfg_file_name is None:
            return f"{WiiSS_Configs.core_file_name.stem}.cfg"
        else:
            return WiiSS_Configs.template_cfg_file_name

    core_file_name = None

    # App 文件夹名称
    app_folder_name = "RA-HEXAECO"

    @staticmethod
    def src_app_directory() -> Path:
        return LocalConfigs.repository_directory.joinpath(
            f"wii\\apps\\{WiiSS_Configs.app_folder_name}"
        )

    # private 文件夹里的数据文件夹名称
    data_folder_name = None

    # .dol 的发布年月日
    release_date = None
