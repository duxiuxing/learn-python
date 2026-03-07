# -- coding: UTF-8 --

from init_global_configs import Init_Global_Configs
from local_configs import LocalConfigs
from pathlib import Path
from wii_ra_app_configs import WiiRA_AppConfigs
from wii_ra_app import WiiRA_App
from wiiflow_configs import WiiFlow_Configs
from wiiflow_game import WiiFlow_Game
from wiiflow_games_db import WiiFlow_GamesDB
from wiiflow_rom import WiiFlow_Rom
from wiiflow_roms_db import WiiFlow_RomsDB


app_configs_list = []


def add_game_app_configs(long_name: str, short_name: str):
    rom_file_path = Path("games").joinpath(
        WiiFlow_Configs.plugin_name().lower(),
        f"{short_name}{WiiFlow_Configs.rom_file_extension()}",
    )
    app_configs = WiiRA_AppConfigs(
        long_name=long_name,
        short_name=short_name,
        rom_file_path_list=[rom_file_path],
    )
    app_configs_list.append(app_configs)


if __name__ == "__main__":
    Init_Global_Configs()

    rom_file_title_list = [
        "1941",
        "cworld2j",
        "dino",
        "captcomm",
        "cawing",
        "dynwar",
        "ffight",
        "forgottn",
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

    rom_file_path_list = []
    for game in sorted(game_list, key=lambda x: x.name):
        rom = WiiFlow_RomsDB.query_rom(game_id=game.id)
        rom_file_path = Path("games").joinpath(
            WiiFlow_Configs.plugin_name().lower(),
            f"{rom.file_title}{WiiFlow_Configs.rom_file_extension()}",
        )
        rom_file_path_list.append(rom_file_path)

    app_configs = WiiRA_AppConfigs(
        long_name="Capcom - CP System I",
        short_name="cps1",
        rom_file_path_list=rom_file_path_list,
    )
    app_configs.long_description = (
        "- Emulator for CPS-1 games based on RetroArch.\n"
        "- Based on a snapshot of the FB Alpha codebase from 2012.\n"
        "- Compatible with FB Alpha v0.2.97.29 ROM sets."
    )
    app_configs_list.append(app_configs)

    add_game_app_configs(
        long_name="1941 - Counter Attack",
        short_name="1941",
    )

    add_game_app_configs(
        long_name="Three Wonders",
        short_name="3wonders",
    )

    add_game_app_configs(
        long_name="Captain Commando",
        short_name="captcomm",
    )

    add_game_app_configs(
        long_name="Carrier Air Wing",
        short_name="cawing",
    )

    add_game_app_configs(
        long_name="Capcom World 2",
        short_name="cworld2j",
    )

    add_game_app_configs(
        long_name="Cadillacs and Dinosaurs",
        short_name="dino",
    )

    add_game_app_configs(
        long_name="Dynasty Wars",
        short_name="dynwar",
    )

    add_game_app_configs(
        long_name="Final Fight",
        short_name="ffight",
    )

    add_game_app_configs(
        long_name="Forgotten Worlds",
        short_name="forgottn",
    )

    add_game_app_configs(
        long_name="Ghouls'n Ghosts",
        short_name="ghouls",
    )

    add_game_app_configs(
        long_name="Knights of the Round",
        short_name="knights",
    )

    add_game_app_configs(
        long_name="The King of Dragons",
        short_name="kod",
    )

    add_game_app_configs(
        long_name="Muscle Bomber Duo",
        short_name="mbombrd",
    )

    add_game_app_configs(
        long_name="The Power Battle CPS-1",
        short_name="megaman",
    )

    add_game_app_configs(
        long_name="Mercs",
        short_name="mercs",
    )

    add_game_app_configs(
        long_name="Magic Sword",
        short_name="msword",
    )

    add_game_app_configs(
        long_name="Mega Twins",
        short_name="mtwins",
    )

    add_game_app_configs(
        long_name="Nemo",
        short_name="nemo",
    )

    add_game_app_configs(
        long_name="Pang! 3",
        short_name="pang3",
    )

    add_game_app_configs(
        long_name="Pnickies",
        short_name="pnickj",
    )

    add_game_app_configs(
        long_name="The Punisher",
        short_name="punisher",
    )

    add_game_app_configs(
        long_name="Quiz & Dragons",
        short_name="qad",
    )

    add_game_app_configs(
        long_name="Quiz Tonosama no Yabou 2",
        short_name="qtono2j",
    )

    add_game_app_configs(
        long_name="Street Fighter 2",
        short_name="sf2",
    )

    add_game_app_configs(
        long_name="Street Fighter 2' CE",
        short_name="sf2ce",
    )

    add_game_app_configs(
        long_name="Street Fighter 2' HF",
        short_name="sf2hf",
    )

    add_game_app_configs(
        long_name="Street Fighter Zero",
        short_name="sfzch",
    )

    add_game_app_configs(
        long_name="Sat. Night Slam Masters",
        short_name="slammast",
    )

    add_game_app_configs(
        long_name="Strider",
        short_name="strider",
    )

    add_game_app_configs(
        long_name="U.N. Squadron",
        short_name="unsquad",
    )

    add_game_app_configs(
        long_name="Varth",
        short_name="varth",
    )

    add_game_app_configs(
        long_name="Willow",
        short_name="willow",
    )

    add_game_app_configs(
        long_name="Warriors of Fate",
        short_name="wof",
    )

    while True:
        export_to_dir = LocalConfigs.export_to_directory()
        print(f"\n即将输出 Wii App 到目标文件夹\n默认目标文件夹路径：{export_to_dir}")
        user_input = input("请确认目标文件夹路径，使用默认路径请直接按回车 > ")
        if len(user_input) > 0:
            export_to_dir = Path(user_input)

        if export_to_dir.exists() and export_to_dir.is_dir():
            LocalConfigs._export_to_directory = export_to_dir
        else:
            print(f"【错误】无效的文件夹路径：{export_to_dir}")
            continue

        print("\n1. 输出 USB App")
        print("2. 输出 SD App")
        print("其他输入表示退出")
        user_input = input("请输入操作的序号 > ")
        try:
            number = int(user_input)
            if number == 1:
                for app_configs in app_configs_list:
                    app_configs.device = WiiRA_AppConfigs.DEVICE_USB
                    usb_app = WiiRA_App(app_configs)
                    usb_app.export_all()
            elif number == 2:
                for app_configs in app_configs_list:
                    app_configs.device = WiiRA_AppConfigs.DEVICE_SD
                    sd_app = WiiRA_App(app_configs)
                    sd_app.export_all()
            else:
                break
        except ValueError:
            break
