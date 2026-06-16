# -- coding: UTF-8 --

from init_global_configs import Init_Global_Configs
from local_configs import LocalConfigs
from pathlib import Path
from ra_playlist import RA_Playlist
from ra_playlist_configs import RA_PlaylistConfigs
from wii_app_configs import Wii_AppConfigs
from wii_app_factory import Wii_AppFactory
from wii_ra_vm_app import WiiRA_VM_App
from wii_ss_app import WiiSS_App

if __name__ == "__main__":
    Init_Global_Configs()

    # G
    Wii_AppFactory.add_game_app_configs(rom_file_title="garou")
    
    # M
    Wii_AppFactory.add_game_app_configs(rom_file_title="matrim")    
    Wii_AppFactory.add_game_app_configs(rom_file_title="mslug3")
    Wii_AppFactory.add_game_app_configs(rom_file_title="mslug4")
    Wii_AppFactory.add_game_app_configs(rom_file_title="mslug5")
    Wii_AppFactory.add_game_app_configs(rom_file_title="mslugx", app_name="Metal Slug X")

    plugin_ra_app_configs = Wii_AppConfigs(
        app_name="SNK - Neo Geo VM",
        app_folder_base_name="neogeo-vm",
        rom=None,
    )
    plugin_ra_app_configs.cfg_file_name="neogeo-vm.cfg"
    plugin_ra_app_configs.long_description = (
        "- Emulator for Neo Geo games larger than 23 MB\n"
        "- Based on a snapshot of the FB Alpha codebase from 2012\n"
        "- Compatible with FB Alpha v0.2.97.29 ROM sets"
    )

    plugin_ss_app_configs = Wii_AppConfigs(
        app_name="RA-SS Neo Geo VM",
        app_folder_base_name="neogeo-vm",
        rom=None,
    )
    plugin_ss_app_configs.cfg_file_name="main.cfg"
    plugin_ss_app_configs.long_description = (
        "- Mod By RunningSnakes based on RA-SS Hexaeco\n"
        "- Emulator for Neo Geo games larger than 23 MB\n"
        "- Based on a snapshot of the FB Alpha codebase from 2012\n"
        "- Compatible with FB Alpha v0.2.97.29 ROM sets"
    )

    while True:
        export_to_dir = LocalConfigs.export_to_directory
        print(f"\n即将导出 Wii App 到目标文件夹\n默认目标文件夹路径：{export_to_dir}")
        user_input = input("请确认目标文件夹路径，使用默认路径请直接按回车 > ")
        if len(user_input) > 0:
            export_to_dir = Path(user_input)

        if export_to_dir.exists() and export_to_dir.is_dir():
            LocalConfigs.export_to_directory = export_to_dir
        else:
            print(f"【错误】无效的文件夹路径：{export_to_dir}")
            continue

        print(
            "\n1. 导出 ROM 文件\n"
            "2. 导出 Game App (RA 核心) 到 wii-ra-apps-sd\n"
            "3. 导出 Wiiflow Plugin App (RA 核心) 到 wiiflow-sd\n"
            "4. 导出 Game App (SS 核心) 到 wii-ss-apps-sd\n"
            "5. 导出 Wiiflow Plugin App (SS 核心) 到 wiiflow-sd\n"
            "6. 导出 Game App (SS 核心) 到 wii-ss-apps-usb\n"
            "其他输入表示退出"
        )
        user_input = input("请输入操作的序号 > ")
        device = None
        try:
            number = int(user_input)
            if number == 1:
                # 导出 ROM 文件
                RA_Playlist(WiiRA_VM_App.init_playlist_configs()).export_rom_files()
            elif number == 2:
                # Game App (RA 核心， SD 版)
                Wii_AppFactory.export_game_ra_vm_apps(Wii_AppConfigs.DEVICE_SD)
            elif number == 3:
                # Wiiflow Plugin App (RA 核心， SD 版)
                plugin_ra_app_configs.device = Wii_AppConfigs.DEVICE_SD
                
                playlist_configs = WiiRA_VM_App.init_playlist_configs()
                playlist_configs.boxarts_folder = None
                playlist_configs.logos_folder = None
                # playlist_configs.snaps_folder = None
                # playlist_configs.titles_folder = None

                WiiRA_VM_App(plugin_ra_app_configs, playlist_configs).export_all()
            elif number == 4:
                # Game App (SS 核心， SD 版)
                Wii_AppFactory.export_game_ss_apps(Wii_AppConfigs.DEVICE_SD)
            elif number == 5:
                # Wiiflow Plugin App (SS 核心， SD 版)
                plugin_ss_app_configs.device = Wii_AppConfigs.DEVICE_SD
                WiiSS_App(plugin_ss_app_configs).export_all()
            elif number == 6:
                # Game App (SS 核心， USB 版)
                Wii_AppFactory.export_game_ss_apps(Wii_AppConfigs.DEVICE_USB)
            else:
                break
        except ValueError:
            break
