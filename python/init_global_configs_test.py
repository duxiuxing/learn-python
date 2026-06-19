# -- coding: UTF-8 --

from init_global_configs import Init_Global_Configs
from local_configs import LocalConfigs
from ra_configs import RA_Configs
from wii_app_configs import Wii_AppConfigs
from wii_ra_configs import WiiRA_Configs
from wii_ss_configs import WiiSS_Configs
from wiiflow_configs import WiiFlow_Configs

if __name__ == "__main__":
    Init_Global_Configs()

    print(
        "LocalConfigs:\n"
        f"\trepository_directory = {LocalConfigs.repository_directory}\n"
        f"\texport_to_directory = {LocalConfigs.export_to_directory}\n"
        f"\timport_from_directory = {LocalConfigs.import_from_directory}\n"
        f"\tretroarch_directory = {LocalConfigs.retroarch_directory}\n"
        f"\tseven_zip_exe_path = {LocalConfigs.seven_zip_exe_path}"
    )

    print(
        "RA_Config:\n"
        f"\tlpl_file_name = {RA_Configs.lpl_file_name}\n"
        f"\troms_win_relative_directory = {RA_Configs.win_roms_relative_directory}\n"
        f"\troms_wii_relative_directory = {RA_Configs.wii_roms_relative_directory}\n"
        f"\tandroid_roms_directory = {RA_Configs.android_roms_directory}\n"
        f"\tipad_roms_directory = {RA_Configs.ipad_roms_directory}\n"
        f"\tps3_roms_directory = {RA_Configs.ps3_roms_directory}\n"
        f"\twin_roms_directory = {RA_Configs.win_roms_directory}\n"
        f"\txbox_roms_directory = {RA_Configs.xbox_roms_directory}"
    )

    print(
        "Wii_AppConfigs:\n"
        f"\tdefault_short_description = {Wii_AppConfigs.default_short_description}"
    )

    print(
        "WiiRA_Configs:\n"
        f"\tcore_file_name = {WiiRA_Configs.core_file_name}\n"
        f"\tcore_info_file_name = {WiiRA_Configs.core_info_file_name}\n"
        f"\tcore_name = {WiiRA_Configs.core_name}\n"
        f"\trelease_date = {WiiRA_Configs.release_date}\n"
        f"\tversion = {WiiRA_Configs.version}\n"
        f"\tremaps_relative_directory = {WiiRA_Configs.remaps_relative_directory}"
    )

    print(
        "WiiSS_Configs:\n"
        f"\tcore_file_name = {WiiSS_Configs.core_file_name}\n"
        f"\tdata_folder_name = {WiiSS_Configs.data_folder_name}\n"
        f"\trelease_date = {WiiSS_Configs.release_date}"
    )

    print("WiiFlow_Configs:\n" f"\tplugin_name = {WiiFlow_Configs.plugin_name}")
