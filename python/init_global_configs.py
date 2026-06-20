# -- coding: UTF-8 --

from local_configs import LocalConfigs
from pathlib import Path
from ra_configs import RA_Configs
from roms_xml import RomsXML
from wii_app_configs import Wii_AppConfigs
from wii_ra_configs import WiiRA_Configs
from wii_ss_configs import WiiSS_Configs
from wiiflow_configs import WiiFlow_Configs
from wiiflow_plugins_data import WiiFlow_PluginsData


class Init_Global_Configs:
    def __init__(self):
        # LocalConfigs
        LocalConfigs.repository_directory = Path(
            "D:\\workspace\\github\\duxiuxing\\r-sam-hexaeco"
        )
        dir0 = "C:\\Users\\duxiu\\AppData\\Roaming\\Dolphin Emulator\\Load\\WiiSDSync"
        dir1 = "D:\\workspace\\github\\R-Sam-1980\\hexaeco"
        dir2 = "X:\\"
        LocalConfigs.export_to_directory = Path(dir1)
        LocalConfigs.import_from_directory = Path(dir2)

        LocalConfigs.retroarch_directory = Path("X:\\RetroArch-Win64")
        LocalConfigs.seven_zip_exe_path = Path("C:\\Program Files\\7-Zip\\7z.exe")
        LocalConfigs.wfc_conv_exe_path = Path(
            "C:\\Program Files\\WFC_conv\\Windows\\wfc_conv.exe"
        )

        # RA_Config
        RA_Configs.lpl_file_name = Path("FBNeo - Arcade Games.lpl")
        RA_Configs.wii_roms_relative_directory = "arcade/fbneo"
        # Wii_AppConfigs
        Wii_AppConfigs.default_short_description = "Arcade Emulator"

        # WiiRA_Configs
        WiiRA_Configs._db_name = Path("FBNeo - Arcade Games.lpl")

        # WiiSS_Configs
        WiiSS_Configs.core_file_name = Path("Arcade FBNEO.dol")
        WiiSS_Configs.data_folder_name = "FBNEO"
        WiiSS_Configs.release_date = "20240308"
        # 宽高比：0=4:3
        WiiSS_Configs.settings_dict["aspect_ratio_index"] = "0"
        WiiSS_Configs.settings_dict["aspect_ratio_index_wide"] = "0"
        # FBNEO 的默认分辨率是 384x224，故使用 23=384x448
        WiiSS_Configs.settings_dict["video_vres"] = "23"

        # WiiFlow_Configs
        WiiFlow_Configs.plugin_name = "FBNEO"
        WiiFlow_Configs.website = "https://github.com/R-Sam-1980/hexaeco"

        WiiFlow_PluginsData()
        RomsXML()
