# -- coding: UTF-8 --

from local_configs import LocalConfigs
from pathlib import Path
from roms_xml import RomsXML
from wii_ra_app_configs import WiiRA_AppConfigs
from wii_ra_configs import WiiRA_Configs
from wii_ra_ss_configs import WiiRA_SS_Configs
from wiiflow_configs import WiiFlow_Configs
from wiiflow_plugins_data import WiiFlow_PluginsData


class Init_Global_Configs:
    def __init__(self):
        # LocalConfigs
        LocalConfigs._repository_directory = Path(
            "D:\\workspace\\github\\R-Sam-1980\\hexaeco"
        )
        LocalConfigs._seven_zip_exe_path = Path("C:\\Program Files\\7-Zip\\7z.exe")
        LocalConfigs._wfc_conv_exe_path = Path(
            "C:\\Program Files\\WFC_conv\\Windows\\wfc_conv.exe"
        )

        # WiiFlow_Configs
        WiiFlow_Configs._plugin_name = "MOVIE"


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
