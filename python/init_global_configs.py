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
            "C:\\workspace\\github\\duxiuxing\\nes-player"
        )
        dir0 = "C:\\Users\\duxiu\\AppData\\Roaming\\Dolphin Emulator\\Load\\WiiSDSync"
        dir1 = "D:\\workspace\\github\\R-Sam-1980\\fc-nes"
        dir2 = "X:\\"
        LocalConfigs.export_to_directory = Path(dir1)
        LocalConfigs.import_from_directory = Path(dir2)

        LocalConfigs.retroarch_directory = Path("X:\\RetroArch-Win64")
        LocalConfigs.seven_zip_exe_path = Path("C:\\Program Files\\7-Zip\\7z.exe")
        LocalConfigs.wfc_conv_exe_path = Path(
            "C:\\Program Files\\WFC_conv\\Windows\\wfc_conv.exe"
        )

        # RA_Config
        RA_Configs.rom_file_extension = ".nes"
        RA_Configs.rom_file_renameable = True
        RA_Configs.lpl_file_name = Path("Nintendo - Nintendo Entertainment System.lpl")
        RA_Configs.win_roms_relative_directory = Path("nintendo\\fc")
        RA_Configs.wii_roms_relative_directory = "nintendo/fc"
        RA_Configs.android_roms_directory = "/storage/emulated/0/nintendo/fc"
        RA_Configs.ipad_roms_directory = "~/Documents/RetroArch/nintendo/fc"
        RA_Configs.ps3_roms_directory = "/dev_hdd0/game/RETROARCH/USRDIR/nintendo/fc"
        RA_Configs.win_roms_directory = Path("X:\\nintendo\\fc")
        RA_Configs.xbox_roms_directory = Path("E:\\nintendo\\fc")

        # Wii_AppConfigs
        Wii_AppConfigs.default_short_description = "Nintendo FCEUmm Emulator"

        # WiiRA_Configs
        WiiRA_Configs.core_file_name = Path("fceumm_libretro_wii.dol")
        WiiRA_Configs.core_info_file_name = Path("fceumm_libretro.info")
        WiiRA_Configs.core_name = "Nintendo - NES / Famicom (FCEUmm)"
        WiiRA_Configs.release_date = "20251120"
        WiiRA_Configs.version = "1.22.2"
        # 任天堂红白机的原生分辨率是 256x224，故使用 27=512x448
        WiiRA_Configs.settings_dict["current_resolution_id"] = "27"

        # WiiSS_Configs
        WiiSS_Configs.core_file_name = Path("Nintendo FCEUmm.dol")
        WiiSS_Configs.data_folder_name = "FCMOD"
        WiiSS_Configs.release_date = "20220508"
        # 宽高比：0=4:3
        WiiSS_Configs.settings_dict["aspect_ratio_index"] = "0"
        WiiSS_Configs.settings_dict["aspect_ratio_index_wide"] = "0"
        # 任天堂红白机的原生分辨率是 256x224，故使用 =512x448
        WiiSS_Configs.settings_dict["video_vres"] = "23"

        # WiiFlow_Configs
        WiiFlow_Configs.plugin_name = "FC"
        WiiFlow_Configs.website = "https://github.com/R-Sam-1980/fc-nes"

        WiiFlow_PluginsData()
        RomsXML()
