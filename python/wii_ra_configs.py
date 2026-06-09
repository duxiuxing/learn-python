# -- coding: UTF-8 --

from local_configs import LocalConfigs
from pathlib import Path


class WiiRA_Configs:
    default_cfg_file_name = Path("retroarch.cfg")

    core_file_name = None
    core_info_file_name = None
    core_name = None

    # Wii 版 RetroArch 的 App 文件夹名称
    @staticmethod
    def src_app_directory() -> Path:
        return LocalConfigs.repository_directory.joinpath(
            f"wii\\apps\\retroarch-wii-v{WiiRA_Configs.version}"
        )

    # Wii 版 RetroArch 的发布年月日，比如 "20251120"
    release_date = None

    # Wii 版 RetroArch 的版本号，比如 "1.22.2"
    version = None

    # ROM 文件所在文件夹的相对路径，比如 Path("arcade\\fba\\cps1")
    rom_relative_folder_win_path = None

    @staticmethod
    def rom_folder_wii_path(device) -> str:
        path = str(WiiRA_Configs.rom_relative_folder_win_path).replace("\\", "/")
        return f"{device}:/{path}"

    @staticmethod
    def data_folder_wii_path(device) -> str:
        return f"{device}:/retroarch"

    settings_list = None
