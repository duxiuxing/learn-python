# -- coding: UTF-8 --

from init_global_configs import Init_Global_Configs
from local_configs import LocalConfigs
from pathlib import Path
from wii_ra_app import WiiRA_App
from wii_app_configs import Wii_AppConfigs
from wii_ra_configs import WiiRA_Configs
from wii_ss_app import WiiSS_App
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

    rom_file_relative_path = WiiRA_Configs.roms_relative_directory().joinpath(
        f"{rom.file_title}{WiiFlow_Configs.rom_file_extension()}",
    )

    app_configs = Wii_AppConfigs(
        app_name=app_name,
        folder_name=rom_file_title,
        rom_file_relative_path_list=[rom_file_relative_path],
    )
    game_app_configs_list.append(app_configs)


if __name__ == "__main__":
    Init_Global_Configs()

    # 基于 retroarch-wii 核心的 App
    rom_file_title_list = [
        "1941",
        "cworld2j",
        "dino",
        "captcomm",
        # "cawing",
        "dynwar",
        "ffight",
        # "forgottn",
        "ghouls",
        "knights",
        "msword",
        "megaman",
        "mtwins",
        "mercs",
        "mbombrd",
        "nemo",
        "pang3",
        "pnickj",
        "qad",
        "qtono2j",
        "slammast",
        "sf2",
        "sf2ce",
        "sf2hf",
        "sfzch",
        "strider",
        "kod",
        "punisher",
        "3wonders",
        "unsquad",
        "varth",
        "wof",
        "willow",
    ]

    game_list = []
    for rom_file_title in rom_file_title_list:
        game_id = WiiFlow_RomsDB.query_rom(rom_file_title=rom_file_title).game_id
        game_list.append(WiiFlow_GamesDB.query_game(game_id=game_id))

    rom_file_relative_path_list = []
    for game in sorted(game_list, key=lambda x: x.name):
        rom = WiiFlow_RomsDB.query_rom(game_id=game.id)
        rom_file_relative_path = WiiRA_Configs.roms_relative_directory().joinpath(
            f"{rom.file_title}{WiiFlow_Configs.rom_file_extension()}",
        )
        rom_file_relative_path_list.append(rom_file_relative_path)

    ra_app_configs = Wii_AppConfigs(
        app_name="Capcom - CP System I",
        folder_name="cps1",
        rom_file_relative_path_list=rom_file_relative_path_list,
    )
    ra_app_configs.long_description = (
        "- Emulator for CPS-1 games based on RetroArch\n"
        "- Based on a snapshot of the FB Alpha codebase from 2012\n"
        "- Compatible with FB Alpha v0.2.97.29 ROM sets"
    )

    # 基于 RA-HEXAECO 核心的 App
    ra_ss_app_configs = Wii_AppConfigs(
        app_name="RA-SS CPS-1",
        folder_name="cps1",
        rom_file_relative_path_list=rom_file_relative_path_list,
    )
    ra_ss_app_configs.long_description = (
        "- Mod By RunningSnakes\n"
        "- Emulator for CPS-1 games based on RA-SS Hexaeco\n"
        "- Based on a snapshot of the FB Alpha codebase from 2012\n"
        "- Compatible with FB Alpha v0.2.97.29 ROM sets"
    )

    add_game_app_configs(rom_file_title="1941")
    add_game_app_configs(rom_file_title="3wonders")
    add_game_app_configs(rom_file_title="captcomm")
    # add_game_app_configs(rom_file_title="cawing")
    add_game_app_configs(rom_file_title="cworld2j", app_name="Capcom World 2")
    add_game_app_configs(rom_file_title="dino")
    add_game_app_configs(rom_file_title="dynwar")
    add_game_app_configs(rom_file_title="ffight")
    # add_game_app_configs(rom_file_title="forgottn")
    add_game_app_configs(rom_file_title="ghouls")
    add_game_app_configs(rom_file_title="knights")
    add_game_app_configs(rom_file_title="kod")
    add_game_app_configs(rom_file_title="mbombrd", app_name="Slam Masters - UTB")
    add_game_app_configs(rom_file_title="megaman", app_name="Mega Man")
    add_game_app_configs(rom_file_title="mercs")
    add_game_app_configs(rom_file_title="msword", app_name="Magic Sword")
    add_game_app_configs(rom_file_title="mtwins")
    add_game_app_configs(rom_file_title="nemo")
    add_game_app_configs(rom_file_title="pang3")
    add_game_app_configs(rom_file_title="pnickj")
    add_game_app_configs(rom_file_title="punisher")
    add_game_app_configs(rom_file_title="qad")
    add_game_app_configs(rom_file_title="qtono2j", app_name="Quiz Tonosama no Yabou 2")
    add_game_app_configs(rom_file_title="sf2", app_name="Street Fighter 2")
    add_game_app_configs(rom_file_title="sf2ce", app_name="Street Fighter 2' CE")
    add_game_app_configs(rom_file_title="sf2hf", app_name="Street Fighter 2' HF")
    add_game_app_configs(rom_file_title="sfzch")
    add_game_app_configs(rom_file_title="slammast", app_name="Slam Masters")
    add_game_app_configs(rom_file_title="strider")
    add_game_app_configs(rom_file_title="unsquad")
    add_game_app_configs(rom_file_title="varth", app_name="Varth")
    add_game_app_configs(rom_file_title="willow")
    add_game_app_configs(rom_file_title="wof")

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

        print(
            "\n1. 导出 App (retroarch-wii 核心) 到 wii-ra-apps-sd\n"
            "2. 导出 App (RA-HEXAECO 核心) 到 wii-ss-apps-sd\n"
            "3. 导出 App (RA-HEXAECO 核心) 到 wii-ss-apps-usb\n"
            "其他输入表示退出"
        )
        user_input = input("请输入操作的序号 > ")
        device = None
        try:
            number = int(user_input)
            if number == 1:
                device = Wii_AppConfigs.DEVICE_SD

                ra_app_configs.device = device
                WiiRA_App(ra_app_configs).export_all()
                for app_configs in game_app_configs_list:
                    app_configs.device = device
                    game_app = WiiRA_App(app_configs)
                    game_app.export_all()
            elif number == 2:
                device = Wii_AppConfigs.DEVICE_SD

                ra_ss_app_configs.device = device
                WiiSS_App(ra_ss_app_configs).export_all()
                for app_configs in game_app_configs_list:
                    app_configs.device = device
                    game_app = WiiSS_App(app_configs)
                    game_app.export_all()
            elif number == 3:
                device = Wii_AppConfigs.DEVICE_USB

                ra_ss_app_configs.device = device
                WiiSS_App(ra_ss_app_configs).export_all()
                for app_configs in game_app_configs_list:
                    app_configs.device = device
                    game_app = WiiSS_App(app_configs)
                    game_app.export_all()
            else:
                break
        except ValueError:
            break
