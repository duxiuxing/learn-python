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


def add_game_app_configs(rom_file_title: str, app_name=None):
    rom = WiiFlow_RomsDB.query_rom(rom_file_title=rom_file_title)
    game = WiiFlow_GamesDB.query_game(rom.game_id)
    if app_name is None:
        app_name = game.name
    elif app_name == game.name:
        print(f"【提示】{rom_file_title} App 无需指定 app_name")

    rom_file_path = Path("games").joinpath(
        WiiFlow_Configs.plugin_name().lower(),
        f"{rom_file_title}{WiiFlow_Configs.rom_file_extension()}",
    )

    app_configs = WiiRA_AppConfigs(
        app_name=app_name,
        folder_name=rom_file_title,
        rom_file_path_list=[rom_file_path],
    )
    app_configs_list.append(app_configs)


if __name__ == "__main__":
    Init_Global_Configs()

    rom_file_title_list = [
        "1944",
        "19xx",
        "armwar",
        "avsp",
        "batcir",
        "choko",
        "csclub",
        "cybots",
        "ddsom",
        "ddtod",
        "dimahoo",
        "dstlk",
        "ecofghtr",
        "gigawing",
        "hsf2",
        "jyangoku",
        "megaman2",
        "mmancp2u",
        "mmatrix",
        "mpang",
        "msh",
        "mshvsf",
        "mvsc",
        "nwarr",
        "progear",
        "pzloop2",
        "qndream",
        "ringdest",
        "sfa",
        "sfa2",
        "sfa3",
        "sfz2al",
        "sgemf",
        "spf2t",
        "ssf2",
        "ssf2t",
        "vhunt2",
        "vsav",
        "vsav2",
        "xmcota",
        "xmvsf",
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
        app_name="Capcom - CP System II",
        folder_name="cps2",
        rom_file_path_list=rom_file_path_list,
    )
    app_configs.long_description = (
        "- Emulator for CPS-2 games based on RetroArch.\n"
        "- Based on a snapshot of the FB Alpha codebase from 2012.\n"
        "- Compatible with FB Alpha v0.2.97.29 ROM sets."
    )
    app_configs_list.append(app_configs)

    add_game_app_configs(rom_file_title="1944")
    add_game_app_configs(rom_file_title="19xx", app_name="19XX")
    add_game_app_configs(rom_file_title="armwar")
    add_game_app_configs(rom_file_title="avsp")
    add_game_app_configs(rom_file_title="batcir")
    add_game_app_configs(rom_file_title="choko")
    add_game_app_configs(rom_file_title="csclub")
    add_game_app_configs(rom_file_title="cybots", app_name="Cyberbots")
    add_game_app_configs(rom_file_title="ddsom", app_name="Dungeons & Dragons 2")
    add_game_app_configs(rom_file_title="ddtod", app_name="Dungeons & Dragons")
    add_game_app_configs(rom_file_title="dimahoo")
    add_game_app_configs(rom_file_title="dstlk", app_name="Darkstalkers")
    add_game_app_configs(rom_file_title="ecofghtr")
    add_game_app_configs(rom_file_title="gigawing")
    add_game_app_configs(rom_file_title="hsf2", app_name="Hyper Street Fighter 2")
    add_game_app_configs(rom_file_title="jyangoku", app_name="Jyangokushi")
    add_game_app_configs(rom_file_title="megaman2", app_name="Mega Man 2")
    add_game_app_configs(rom_file_title="mmancp2u", app_name="Mega Man for CPS-2")
    add_game_app_configs(rom_file_title="mmatrix", app_name="Mars Matrix")
    add_game_app_configs(rom_file_title="mpang")
    add_game_app_configs(rom_file_title="msh")
    add_game_app_configs(rom_file_title="mshvsf", app_name="Marvel vs. Street Fighter")
    add_game_app_configs(rom_file_title="mvsc", app_name="Marvel vs. Capcom")
    add_game_app_configs(rom_file_title="nwarr", app_name="Vampire Hunter")
    add_game_app_configs(rom_file_title="progear")
    add_game_app_configs(rom_file_title="pzloop2")
    add_game_app_configs(rom_file_title="qndream", app_name="Quiz Nanairo Dreams")
    add_game_app_configs(rom_file_title="ringdest", app_name="Slam Masters 2")
    add_game_app_configs(rom_file_title="sfa", app_name="Street Fighter Alpha")
    add_game_app_configs(rom_file_title="sfa2")
    add_game_app_configs(rom_file_title="sfa3")
    add_game_app_configs(rom_file_title="sfz2al")
    add_game_app_configs(rom_file_title="sgemf", app_name="Super Gem Fighter")
    add_game_app_configs(rom_file_title="spf2t", app_name="Super Puzzle Fighter")
    add_game_app_configs(rom_file_title="ssf2", app_name="Super Street Fighter 2")
    add_game_app_configs(rom_file_title="ssf2t", app_name="Super Street Fighter 2T")
    add_game_app_configs(rom_file_title="vhunt2", app_name="Vampire Hunter 2")
    add_game_app_configs(rom_file_title="vsav", app_name="Vampire Savior")
    add_game_app_configs(rom_file_title="vsav2", app_name="Vampire Savior 2")
    add_game_app_configs(rom_file_title="xmcota", app_name="X-Men")
    add_game_app_configs(rom_file_title="xmvsf")

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
