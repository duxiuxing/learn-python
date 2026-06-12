# -- coding: UTF-8 --

from init_global_configs import Init_Global_Configs
from local_configs import LocalConfigs
from pathlib import Path
from ra_playlist import RA_Playlist
from ra_playlist_configs import RA_PlaylistConfigs
from wii_app_configs import add_game_app_configs
from wii_app_configs import game_app_configs_list
from wii_app_configs import Wii_AppConfigs
from wii_ra_app import WiiRA_App

if __name__ == "__main__":
    Init_Global_Configs()

    cps3_ra_app_configs = Wii_AppConfigs(
        app_name="Capcom - CP System III",
        base_app_folder_name="cps3",
        rom=None,
    )
    cps3_ra_app_configs.long_description = (
        "- Emulator for CPS-3 games based on RetroArch\n"
        "- Based on a snapshot of the FB Alpha codebase from 2012\n"
        "- Compatible with FB Alpha v0.2.97.29 ROM sets"
    )

    add_game_app_configs(rom_file_title="jojo", remap="jojo")
    add_game_app_configs(
        rom_file_title="jojoba", app_name="JoJo's Venture 2", remap="jojo"
    )
    add_game_app_configs(rom_file_title="redearth")
    add_game_app_configs(rom_file_title="sfiii", app_name="Street Fighter 3.1")
    add_game_app_configs(rom_file_title="sfiii2", app_name="Street Fighter 3.2")
    add_game_app_configs(rom_file_title="sfiii3", app_name="Street Fighter 3.3")

    while True:
        export_to_dir = LocalConfigs.export_to_directory
        print(f"\n即将导出 Wii App 到目标文件夹\n默认目标文件夹路径：{export_to_dir}")
        user_input = input("请确认目标文件夹路径，使用默认路径请直接按回车 > ")
        if len(user_input) > 0:
            export_to_dir = Path(user_input)

        if export_to_dir.exists() and export_to_dir.is_dir():
            LocalConfigs._export_to_directory = export_to_dir
        else:
            print(f"【错误】无效的文件夹路径：{export_to_dir}")
            continue

        print(
            "\n1. 导出 ROM 文件\n"
            "2. 导出 App (retroarch-wii 核心) 到 wii-ra-apps-sd\n"
            "其他输入表示退出"
        )
        user_input = input("请输入操作的序号 > ")
        device = None
        try:
            number = int(user_input)
            if number == 1:
                cps3_ra_app_configs.init_playlist_configs()
                RA_Playlist(cps3_ra_app_configs.playlist_configs).export_rom_files()
            elif number == 2:
                device = Wii_AppConfigs.DEVICE_SD

                cps3_ra_app_configs.device = device
                cps3_ra_app_configs.init_playlist_configs()
                cps3_ra_app_configs.playlist_configs.boxarts_folder = None
                cps3_ra_app_configs.playlist_configs.logos_folder = None
                cps3_ra_app_configs.playlist_configs.snaps_folder = None
                cps3_ra_app_configs.playlist_configs.titles_folder = None
                cps3_ra_app_configs.use_favorites_as_playlist = True
                WiiRA_App(cps3_ra_app_configs).export_all()

                for game_app_configs in game_app_configs_list:
                    game_app_configs.device = device
                    game_app = WiiRA_App(game_app_configs)
                    game_app.export_all()
            else:
                break
        except ValueError:
            break
