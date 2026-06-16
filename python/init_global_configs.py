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
            "C:\\workspace\\github\\duxiuxing\\r-sam-neogeo"
        )
        dir0 = "C:\\Users\\duxiu\\AppData\\Roaming\\Dolphin Emulator\\Load\\WiiSDSync"
        dir1 = "D:\\workspace\\github\\R-Sam-1980\\neogeo"
        dir2 = "X:\\"
        LocalConfigs.export_to_directory = Path(dir1)
        LocalConfigs.import_from_directory = Path(dir2)

        LocalConfigs.retroarch_directory = Path("X:\\RetroArch-Win64")
        LocalConfigs.seven_zip_exe_path = Path("C:\\Program Files\\7-Zip\\7z.exe")
        LocalConfigs.wfc_conv_exe_path = Path(
            "C:\\Program Files\\WFC_conv\\Windows\\wfc_conv.exe"
        )

        # RA_Config
        RA_Configs.lpl_file_name = Path("SNK - Neo Geo.lpl")
        RA_Configs.win_roms_relative_directory = Path("arcade\\neogeo")
        RA_Configs.wii_roms_relative_directory = "arcade/fba/neogeo-vm"
        RA_Configs.android_roms_directory = "/storage/emulated/0/arcade/neogeo"
        RA_Configs.ipad_roms_directory = "~/Documents/RetroArch/arcade/neogeo"
        RA_Configs.ps3_roms_directory = "/dev_hdd0/game/RETROARCH/USRDIR/arcade/neogeo"
        RA_Configs.win_roms_directory = Path("X:\\arcade\\neogeo")
        RA_Configs.xbox_roms_directory = Path("E:\\arcade\\neogeo")

        # Wii_AppConfigs
        Wii_AppConfigs.default_short_description = "SNK Neo Geo VM Emulator"

        # WiiRA_Configs
        WiiRA_Configs.core_file_name = Path("fbalpha2012_neogeo_libretro_wii.dol")
        WiiRA_Configs.core_info_file_name = Path("fbalpha2012_neogeo_libretro.info")
        WiiRA_Configs.core_name = "Arcade (FB Alpha 2012 Neo Geo)"
        WiiRA_Configs.release_date = "20200116"
        WiiRA_Configs.version = "1.8.4"
        WiiRA_Configs.settings_list = [
            # NeoGeo 的原生分辨率是 320x224，故使用 30=640x448
            'current_resolution_id = "30"'
        ]
        WiiRA_Configs.remaps_relative_directory = Path(
            "retroarch\\remaps\\FB Alpha 2012 Neo Geo"
        )

        # WiiSS_Configs
        WiiSS_Configs.core_file_name = Path("Arcade NEO VM.dol")
        WiiSS_Configs.data_folder_name = "NGMOD"
        WiiSS_Configs.release_date = "20220508"
        WiiSS_Configs.settings_list = [
            # 宽高比：0=4:3
            'aspect_ratio_index = "0"',
            'aspect_ratio_index_wide = "0"',
            # NeoGeo 的原生分辨率是 320x224，故使用 29=640x448
            'video_vres = "29"',
        ]

        # WiiFlow_Configs
        WiiFlow_Configs.plugin_name = "NEOGEO-VM"
        WiiFlow_Configs.website = "https://github.com/R-Sam-1980/neogeo"

        WiiFlow_PluginsData()
        RomsXML()
