# -- coding: UTF-8 --

from local_configs import LocalConfigs
from pathlib import Path
from ra_configs import RA_Configs


class WiiRA_Configs:
    template_cfg_file_name = Path("retroarch.cfg")

    core_file_name = None
    core_info_file_name = None
    core_name = None

    @staticmethod
    def repository_directory() -> Path:
        return LocalConfigs.repository_directory.joinpath(
            f"wii\\retroarch-wii-v{WiiRA_Configs.version}"
        )

    # 设备根目录的 retroarch 文件夹
    data_folder_name = "retroarch"

    @staticmethod
    def win_data_directory() -> Path:
        return LocalConfigs.export_to_directory.joinpath(WiiRA_Configs.data_folder_name)

    @staticmethod
    def wii_data_directory(wii_device) -> str:
        return f"{wii_device}:/{WiiRA_Configs.data_folder_name}"

    # Wii 版 RetroArch 发布的年月日，比如 "20251120"
    release_date = None

    # Wii 版 RetroArch 的版本号，比如 "1.22.2"
    version = None

    @staticmethod
    def wii_roms_directory(device) -> str:
        return f"{device}:/{RA_Configs.wii_roms_relative_directory}"

    @staticmethod
    def wii_data_directory(device) -> str:
        return f"{device}:/retroarch"

    settings_dict = {}

    remaps_relative_directory = None
