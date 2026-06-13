# -- coding: UTF-8 --

from local_configs import LocalConfigs
from pathlib import Path
from ra_configs import RA_Configs
from roms_xml import RomsXML
from wii_app_configs import Wii_AppConfigs
from wii_ra_configs import WiiRA_Configs
from wiiflow_configs import WiiFlow_Configs
from wiiflow_plugins_data import WiiFlow_PluginsData


class Init_Global_Configs:
    def __init__(self):
        # LocalConfigs
        LocalConfigs.repository_directory = Path(
            "C:\\workspace\\github\\duxiuxing\\r-sam-cps3"
        )
        dir0 = "C:\\Users\\duxiu\\AppData\\Roaming\\Dolphin Emulator\\Load\\WiiSDSync"
        dir1 = "D:\\workspace\\github\\R-Sam-1980\\cps3"
        dir2 = "X:\\"
        LocalConfigs.export_to_directory = Path(dir1)

        LocalConfigs.retroarch_directory = Path("X:\\RetroArch-Win64")
        LocalConfigs.seven_zip_exe_path = Path("C:\\Program Files\\7-Zip\\7z.exe")
        LocalConfigs.wfc_conv_exe_path = Path(
            "C:\\Program Files\\WFC_conv\\Windows\\wfc_conv.exe"
        )

        # RA_Config
        RA_Configs.lpl_file_name = Path("Capcom - CP System III.lpl")
        RA_Configs.win_roms_relative_directory = Path("arcade\\cps3")
        RA_Configs.wii_roms_relative_directory = "arcade/fba/cps3"
        RA_Configs.android_roms_directory = Path("/storage/emulated/0/arcade/cps3")
        RA_Configs.ipad_roms_directory = Path("~/Documents/RetroArch/arcade/cps3")
        RA_Configs.ps3_roms_directory = Path(
            "/dev_hdd0/game/RETROARCH/USRDIR/arcade/cps3"
        )
        RA_Configs.win_roms_directory = Path("X:\\arcade\\cps3")
        RA_Configs.xbox_roms_directory = Path("E:\\arcade\\cps3")

        # Wii_AppConfigs
        Wii_AppConfigs.default_short_description = "Capcom Play System 3 Emulator"

        # WiiRA_Configs
        WiiRA_Configs.core_file_name = Path("fbalpha2012_cps3_libretro_wii.dol")
        WiiRA_Configs.core_info_file_name = Path("fbalpha2012_cps3_libretro.info")
        WiiRA_Configs.core_name = "Arcade (FB Alpha 2012 CPS-3)"
        WiiRA_Configs.release_date = "20251120"
        WiiRA_Configs.version = "1.22.2"
        WiiRA_Configs.settings_list = [
            # CPS3 的原生分辨率是 384x224，故使用 24=384x448
            'current_resolution_id = "24"'
        ]
        WiiRA_Configs.remaps_relative_directory = Path(
            "remaps\\FB Alpha 2012 CPS-3"
        )

        # WiiFlow_Configs
        WiiFlow_Configs.plugin_name = "CPS3"
        WiiFlow_Configs.website = "https://github.com/R-Sam-1980/cps3"

        WiiFlow_PluginsData()
        RomsXML()
