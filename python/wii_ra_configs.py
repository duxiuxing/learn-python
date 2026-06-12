# -- coding: UTF-8 --

from local_configs import LocalConfigs
from pathlib import Path
from ra_configs import RA_Configs


class WiiRA_Configs:
    default_cfg_file_name = Path("retroarch.cfg")

    core_file_name = None
    core_info_file_name = None
    core_name = None

    @staticmethod
    def repository_directory() -> Path:
        return LocalConfigs.repository_directory.joinpath(
            f"wii\\retroarch-wii-v{WiiRA_Configs.version}"
        )

    # Wii 版 RetroArch 的发布年月日，比如 "20251120"
    release_date = None

    # Wii 版 RetroArch 的版本号，比如 "1.22.2"
    version = None

    @staticmethod
    def wii_roms_directory(device) -> str:
        return f"{device}:/{RA_Configs.wii_roms_relative_directory}"

    @staticmethod
    def wii_data_directory(device) -> str:
        return f"{device}:/retroarch"

    settings_list = None

    wii_remaps_relative_directory = None
