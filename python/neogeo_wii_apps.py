# -- coding: UTF-8 --

from init_global_configs import Init_Global_Configs
from local_configs import LocalConfigs
from pathlib import Path
from ra_playlist import RA_Playlist
from ra_playlist_configs import RA_PlaylistConfigs
from wii_app_configs import Wii_AppConfigs
from wii_app_factory import Wii_AppFactory
from wii_ra_app import WiiRA_App
from wii_ss_app import WiiSS_App

if __name__ == "__main__":
    Init_Global_Configs()

    # #
    Wii_AppFactory.add_game_app_configs(rom_file_title="2020bb")
    Wii_AppFactory.add_game_app_configs(rom_file_title="3countb")
    # A
    Wii_AppFactory.add_game_app_configs(rom_file_title="alpham2")
    Wii_AppFactory.add_game_app_configs(rom_file_title="androdun")
    Wii_AppFactory.add_game_app_configs(rom_file_title="aodk")
    Wii_AppFactory.add_game_app_configs(rom_file_title="aof")
    Wii_AppFactory.add_game_app_configs(rom_file_title="aof2")
    Wii_AppFactory.add_game_app_configs(rom_file_title="aof3")
    Wii_AppFactory.add_game_app_configs(rom_file_title="sonicwi2")
    Wii_AppFactory.add_game_app_configs(rom_file_title="sonicwi3")
    # B
    Wii_AppFactory.add_game_app_configs(rom_file_title="b2buster")
    Wii_AppFactory.add_game_app_configs(rom_file_title="bakatono", app_name="Mahjong 3")
    Wii_AppFactory.add_game_app_configs(rom_file_title="bangbead")
    Wii_AppFactory.add_game_app_configs(rom_file_title="bjourney")
    Wii_AppFactory.add_game_app_configs(rom_file_title="blazstar")
    Wii_AppFactory.add_game_app_configs(rom_file_title="breakers")
    Wii_AppFactory.add_game_app_configs(rom_file_title="breakrev")
    Wii_AppFactory.add_game_app_configs(rom_file_title="bstars")
    Wii_AppFactory.add_game_app_configs(rom_file_title="bstars2")
    Wii_AppFactory.add_game_app_configs(rom_file_title="burningf")
    Wii_AppFactory.add_game_app_configs(rom_file_title="flipshot")
    # C
    Wii_AppFactory.add_game_app_configs(rom_file_title="crsword")
    Wii_AppFactory.add_game_app_configs(rom_file_title="ctomaday")
    Wii_AppFactory.add_game_app_configs(rom_file_title="cyberlip")
    Wii_AppFactory.add_game_app_configs(rom_file_title="marukodq")
    # D
    Wii_AppFactory.add_game_app_configs(rom_file_title="doubledr")
    # E
    Wii_AppFactory.add_game_app_configs(rom_file_title="eightman")
    # F
    Wii_AppFactory.add_game_app_configs(rom_file_title="fatfursp")
    Wii_AppFactory.add_game_app_configs(rom_file_title="fatfury1")
    Wii_AppFactory.add_game_app_configs(rom_file_title="fatfury2")
    Wii_AppFactory.add_game_app_configs(rom_file_title="fatfury3")
    Wii_AppFactory.add_game_app_configs(rom_file_title="fbfrenzy")
    Wii_AppFactory.add_game_app_configs(rom_file_title="fightfev")
    Wii_AppFactory.add_game_app_configs(rom_file_title="kabukikl")
    # M
    # add_game_app_configs(rom_file_title="magdrop2")
    # add_game_app_configs(rom_file_title="magdrop3")
    # add_game_app_configs(rom_file_title="maglord")
    # add_game_app_configs(rom_file_title="mahretsu", app_name="Mahjong 2")
    # add_game_app_configs(rom_file_title="miexchng")
    # add_game_app_configs(rom_file_title="minasan", app_name="Mahjong 1")
    # add_game_app_configs(rom_file_title="mslug", app_name="Metal Slug")
    # add_game_app_configs(rom_file_title="mslug2", app_name="Metal Slug 2")
    # add_game_app_configs(rom_file_title="mutnat")

    plugin_ra_app_configs = Wii_AppConfigs(
        app_name="SNK - Neo Geo",
        app_folder_base_name="neogeo",
        rom=None,
    )
    plugin_ra_app_configs.long_description = (
        "- Emulator for Neo Geo games smaller than 23 MB\n"
        "- Based on a snapshot of the FB Alpha codebase from 2012\n"
        "- Compatible with FB Alpha v0.2.97.29 ROM sets"
    )

    plugin_ss_app_configs = Wii_AppConfigs(
        app_name="RA-SS Neo Geo",
        app_folder_base_name="neogeo",
        rom=None,
    )
    plugin_ss_app_configs.cfg_file_name = "main.cfg"
    plugin_ss_app_configs.long_description = (
        "- Mod By RunningSnakes based on RA-SS Hexaeco\n"
        "- Emulator for Neo Geo games smaller than 23 MB\n"
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
                RA_Playlist(WiiRA_App.init_playlist_configs()).export_rom_files()
            elif number == 2:
                # Game App (RA 核心， SD 版)
                Wii_AppFactory.export_game_ra_apps(Wii_AppConfigs.DEVICE_SD)
            elif number == 3:
                # Wiiflow Plugin App (RA 核心， SD 版)
                plugin_ra_app_configs.device = Wii_AppConfigs.DEVICE_SD

                playlist_configs = WiiRA_App.init_playlist_configs()
                playlist_configs.boxarts_folder = None
                playlist_configs.logos_folder = None
                playlist_configs.snaps_folder = None
                playlist_configs.titles_folder = None

                WiiRA_App(plugin_ra_app_configs, playlist_configs).export_all()
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
