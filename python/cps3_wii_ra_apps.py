# -- coding: UTF-8 --

from init_global_configs import Init_Global_Configs
from local_configs import LocalConfigs
from pathlib import Path
from wii_ra_app import WiiRA_App
from wii_ra_app_configs import WiiRA_AppConfigs
from wii_ra_configs import WiiRA_Configs
from wiiflow_configs import WiiFlow_Configs
from wiiflow_game import WiiFlow_Game
from wiiflow_games_db import WiiFlow_GamesDB
from wiiflow_rom import WiiFlow_Rom
from wiiflow_roms_db import WiiFlow_RomsDB


game_app_configs_list = []


def add_game_app_configs(rom_file_title: str, app_name=None):
    rom = WiiFlow_RomsDB.query_rom(rom_file_title=rom_file_title)
    game = WiiFlow_GamesDB.query_game(rom.game_id)
    if app_name is None:
        app_name = game.name
    elif app_name == game.name:
        print(f"【提示】{rom_file_title} App 无需指定 app_name")

    rom_file_path = WiiRA_Configs.roms_directory().joinpath(
        f"{rom.file_title}{WiiFlow_Configs.rom_file_extension()}",
    )

    app_configs = WiiRA_AppConfigs(
        app_name=app_name,
        folder_name=rom_file_title,
        rom_file_path_list=[rom_file_path],
    )
    game_app_configs_list.append(app_configs)


if __name__ == "__main__":
    Init_Global_Configs()

    rom_file_title_list = [
        "jojoba",
        "jojo",
        "redearth",
        "sfiii",
        "sfiii2",
        "sfiii3",
    ]

    game_list = []
    for rom_file_title in rom_file_title_list:
        game_id = WiiFlow_RomsDB.query_rom(rom_file_title=rom_file_title).game_id
        game_list.append(WiiFlow_GamesDB.query_game(game_id=game_id))

    rom_file_path_list = []
    for game in sorted(game_list, key=lambda x: x.name):
        rom = WiiFlow_RomsDB.query_rom(game_id=game.id)
        rom_file_path = WiiRA_Configs.roms_directory().joinpath(
            f"{rom.file_title}{WiiFlow_Configs.rom_file_extension()}",
        )
        rom_file_path_list.append(rom_file_path)

    app_configs = WiiRA_AppConfigs(
        app_name="Capcom - CP System III",
        folder_name="cps3",
        rom_file_path_list=rom_file_path_list,
    )
    app_configs.long_description = (
        "- Emulator for CPS-3 games based on RetroArch\n"
        "- Based on a snapshot of the FB Alpha codebase from 2012\n"
        "- Compatible with FB Alpha v0.2.97.29 ROM sets"
    )
    game_app_configs_list.append(app_configs)

    add_game_app_configs(rom_file_title="jojoba", app_name="JoJo's Venture 2")
    add_game_app_configs(rom_file_title="jojo")
    add_game_app_configs(rom_file_title="redearth")
    add_game_app_configs(rom_file_title="sfiii", app_name="Street Fighter 3.1")
    add_game_app_configs(rom_file_title="sfiii2", app_name="Street Fighter 3.2")
    add_game_app_configs(rom_file_title="sfiii3", app_name="Street Fighter 3.3")

    while True:
        export_to_dir = LocalConfigs.export_to_directory()
        print(f"\n即将导出 Wii App 到目标文件夹\n默认目标文件夹路径：{export_to_dir}")
        user_input = input("请确认目标文件夹路径，使用默认路径请直接按回车 > ")
        if len(user_input) > 0:
            export_to_dir = Path(user_input)

        if export_to_dir.exists() and export_to_dir.is_dir():
            LocalConfigs._export_to_directory = export_to_dir
        else:
            print(f"【错误】无效的文件夹路径：{export_to_dir}")
            continue

        print("\n1. 导出 USB App\n2. 导出 SD App\n其他输入表示退出")
        user_input = input("请输入操作的序号 > ")
        device = None
        try:
            number = int(user_input)
            if number == 1:
                device = WiiRA_AppConfigs.DEVICE_USB
            elif number == 2:
                device = WiiRA_AppConfigs.DEVICE_SD
            else:
                break

            for app_configs in game_app_configs_list:
                app_configs.device = device
                ra_app = WiiRA_App(app_configs)
                ra_app.export_all()
        except ValueError:
            break
