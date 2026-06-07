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
            "C:\\workspace\\github\\duxiuxing\\r-sam-cps1"
        )
        dir0 = "C:\\Users\\duxiu\\AppData\\Roaming\\Dolphin Emulator\\Load\\WiiSDSync"
        dir1 = "D:\\workspace\\github\\R-Sam-1980\\cps1"
        dir2 = "X:\\"
        LocalConfigs.export_to_directory = Path(dir1)
        LocalConfigs.import_from_directory = Path(dir2)

        LocalConfigs.retroarch_directory = Path("X:\\RetroArch-Win64")
        LocalConfigs.seven_zip_exe_path = Path("C:\\Program Files\\7-Zip\\7z.exe")
        LocalConfigs.wfc_conv_exe_path = Path(
            "C:\\Program Files\\WFC_conv\\Windows\\wfc_conv.exe"
        )

        # RA_Config
        RA_Configs._lpl_file_name = Path("Capcom - CP System I.lpl")
        RA_Configs._roms_relative_directory = Path("arcade\\cps1")

        # WiiRA_AppConfigs
        Wii_AppConfigs._default_short_description = "Capcom Play System 1 Emulator"

        # WiiRA_Configs
        WiiRA_Configs.core_file_name = Path("fbalpha2012_cps1_libretro_wii.dol")
        WiiRA_Configs.core_info_file_name = Path("fbalpha2012_cps1_libretro.info")
        WiiRA_Configs.core_name = "Arcade (FB Alpha 2012 CPS-1)"
        WiiRA_Configs.release_date = "20251120"
        WiiRA_Configs.version = "1.22.2"
        WiiRA_Configs.rom_relative_folder_win_path = Path("arcade\\fba\\cps1")
        WiiRA_Configs.settings_list = [
            # CPS1 的原生分辨率是 384x224，故使用 24=384x448
            'current_resolution_id = "24"'
        ]

        # WiiRA_SS_Configs
        WiiSS_Configs.core_file_name = Path("Arcade CPS1.dol")
        WiiSS_Configs.data_folder_name = "C1MOD"
        WiiSS_Configs.release_date = "20220508"

        # WiiFlow_Configs
        WiiFlow_Configs.plugin_name = "CPS1"
        WiiFlow_Configs.website = "https://github.com/R-Sam-1980/cps1"

        WiiFlow_PluginsData()
        RomsXML()


if __name__ == "__main__":
    Init_Global_Configs()

    print("LocalConfigs:")
    print(f"\trepository_directory = {LocalConfigs.repository_directory}")
    print(f"\texport_to_directory = {LocalConfigs.export_to_directory}")
    print(f"\tretroarch_directory = {LocalConfigs.retroarch_directory}")
    print(f"\tseven_zip_exe_path = {LocalConfigs.seven_zip_exe_path}")

    print("WiiRA_AppConfigs:")
    print(f"\tdefault_short_description = {Wii_AppConfigs._default_short_description}")

    print("WiiRA_Configs:")
    print(f"\tcore_name = {WiiRA_Configs.core_name}")
    print(f"\tcore_file_name = {WiiRA_Configs.core_file_name}")
    print(f"\tcore_info_file_name = {WiiRA_Configs.core_info_file_name}")
    print(f"\trelease_date = {WiiRA_Configs.release_date}")
    print(
        f"\trom_relative_folder_win_path = {WiiRA_Configs.rom_relative_folder_win_path}"
    )
    print(f"\tversion = {WiiRA_Configs.version}")

    print("WiiFlow_Configs:")
    print(f"\tplugin_name = {WiiFlow_Configs.plugin_name}")
