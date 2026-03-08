# -- coding: UTF-8 --

from local_configs import LocalConfigs
from pathlib import Path
from roms_xml import RomsXML
from wii_ra_app_configs import WiiRA_AppConfigs
from wii_ra_configs import WiiRA_Configs
from wiiflow_configs import WiiFlow_Configs
from wiiflow_plugins_data import WiiFlow_PluginsData


class Init_Global_Configs:
    def __init__(self):
        # LocalConfigs
        LocalConfigs._repository_directory = Path(
            "C:\\workspace\\github\\duxiuxing\\r-sam-cps2"
        )
        dir0 = "C:\\Users\\duxiu\\AppData\\Roaming\\Dolphin Emulator\\Load\\WiiSDSync"
        dir1 = "D:\\workspace\\github\\R-Sam-1980\\cps2"
        dir2 = "X:\\"
        LocalConfigs._export_to_directory = Path(dir1)
        LocalConfigs._import_from_directory = Path(dir2)

        LocalConfigs._retroarch_directory = Path("X:\\RetroArch-Win64")
        LocalConfigs._seven_zip_exe_path = Path("C:\\Program Files\\7-Zip\\7z.exe")

        # WiiRA_AppConfigs
        WiiRA_AppConfigs._default_short_description = "Capcom Play System 2 Emulator"

        # WiiRA_Configs
        WiiRA_Configs._core_name = "Arcade (FB Alpha 2012 CPS-2)"
        WiiRA_Configs._core_file_name = Path("fbalpha2012_cps2_libretro_wii.dol")
        WiiRA_Configs._core_info_file_name = Path("fbalpha2012_cps2_libretro.info")
        WiiRA_Configs._db_name = Path("Capcom - CP System II.lpl")
        WiiRA_Configs._release_date = "2025-11-20 10:41"
        WiiRA_Configs._version = "1.22.2"

        # WiiFlow_Configs
        WiiFlow_Configs._plugin_name = "CPS2"

        WiiFlow_PluginsData()
        RomsXML()


if __name__ == "__main__":
    Init_Global_Configs()

    print("LocalConfigs:")
    print(f"\trepository_directory = {LocalConfigs.repository_directory()}")
    print(f"\texport_to_directory = {LocalConfigs.export_to_directory()}")
    print(f"\tretroarch_directory = {LocalConfigs.retroarch_directory()}")
    print(f"\tseven_zip_exe_path = {LocalConfigs.seven_zip_exe_path()}")

    print("WiiRA_AppConfigs:")
    print(
        f"\tdefault_short_description = {WiiRA_AppConfigs._default_short_description}"
    )

    print("WiiRA_Configs:")
    print(f"\tcore_name = {WiiRA_Configs.core_name()}")
    print(f"\tcore_file_name = {WiiRA_Configs.core_file_name()}")
    print(f"\tcore_info_file_name = {WiiRA_Configs.core_info_file_name()}")
    print(f"\tdb_name = {WiiRA_Configs.db_name()}")
    print(f"\trelease_date = {WiiRA_Configs.release_date()}")
    print(f"\tversion = {WiiRA_Configs.version()}")

    print("WiiFlow_Configs:")
    print(f"\tplugin_name = {WiiFlow_Configs.plugin_name()}")
