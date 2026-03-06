# -- coding: UTF-8 --

from init_global_configs import Init_Global_Configs
from local_configs import LocalConfigs
from pathlib import Path
from wii_ra_app_configs import WiiRA_AppConfigs
from wii_ra_app import WiiRA_App
from wiiflow_configs import WiiFlow_Configs


def game_app_configs(long_name: str, short_name: str):
    rom_file_path = Path("games").joinpath(
        WiiFlow_Configs.plugin_name().lower(),
        f"{short_name}{WiiFlow_Configs.rom_file_extension()}",
    )
    return WiiRA_AppConfigs(
        long_name=long_name,
        short_name=short_name,
        rom_file_path_list=[rom_file_path],
    )


if __name__ == "__main__":
    Init_Global_Configs()

    app_configs_list = []

    rom_file_list = [
        "3countb.zip",
        "2020bb.zip",
        "alpham2.zip",
        "androdun.zip",
        "aodk.zip",
        "aof.zip",
        "aof2.zip",
        "aof3.zip",
        "sonicwi2.zip",
        "sonicwi3.zip",
        "b2buster.zip",
        "bakatono.zip",
        "bangbead.zip",
        "bjourney.zip",
        "blazstar.zip",
        "breakers.zip",
        "breakrev.zip",
        "bstars.zip",
        "bstars2.zip",
        "burningf.zip",
        "flipshot.zip",
        "magdrop2.zip",
        "magdrop3.zip",
        "maglord.zip",
        "mahretsu.zip",
        "miexchng.zip",
        "minasan.zip",
        "mslug.zip",
        "mslug2.zip",
        "mutnat.zip",
    ]
    rom_file_path_list = []
    for rom_file_name in rom_file_list:
        rom_file_path = Path("games").joinpath(
            WiiFlow_Configs.plugin_name().lower(),
            rom_file_name,
        )
        rom_file_path_list.append(rom_file_path)
    app_configs = WiiRA_AppConfigs(
        long_name="SNK - Neo Geo",
        short_name="neogeo",
        rom_file_path_list=rom_file_path_list,
    )
    app_configs.long_description = (
        "- Emulator for Neo Geo games smaller than 23 MB.\n"
        "- Based on a snapshot of the FB Alpha codebase from circa 2012.\n"
        "- Compatible with FB Alpha v0.2.97.29 ROM sets."
    )
    app_configs_list.append(app_configs)

    app_configs = game_app_configs(
        long_name="3 Count Bout",
        short_name="3countb",
    )
    app_configs_list.append(app_configs)

    app_configs = game_app_configs(
        long_name="2020 Super Baseball",
        short_name="2020bb",
    )
    app_configs_list.append(app_configs)

    app_configs = game_app_configs(
        long_name="Alpha Mission II",
        short_name="alpham2",
    )
    app_configs_list.append(app_configs)

    app_configs = game_app_configs(
        long_name="Andro Dunos",
        short_name="androdun",
    )
    app_configs_list.append(app_configs)

    app_configs = game_app_configs(
        long_name="Aggressors of Dark Kombat",
        short_name="aodk",
    )
    app_configs_list.append(app_configs)

    app_configs = game_app_configs(
        long_name="Art of Fighting",
        short_name="aof",
    )
    app_configs_list.append(app_configs)

    app_configs = game_app_configs(
        long_name="Art of Fighting 2",
        short_name="aof2",
    )
    app_configs_list.append(app_configs)

    app_configs = game_app_configs(
        long_name="Art of Fighting 3",
        short_name="aof3",
    )
    app_configs_list.append(app_configs)

    app_configs = game_app_configs(
        long_name="Aero Fighters 2",
        short_name="sonicwi2",
    )
    app_configs_list.append(app_configs)

    app_configs = game_app_configs(
        long_name="Aero Fighters 3",
        short_name="sonicwi3",
    )
    app_configs_list.append(app_configs)

    app_configs = game_app_configs(
        long_name="Bang Bang Busters",
        short_name="b2buster",
    )
    app_configs_list.append(app_configs)

    app_configs = game_app_configs(
        long_name="Mahjong 3",
        short_name="bakatono",
    )
    app_configs_list.append(app_configs)

    app_configs = game_app_configs(
        long_name="Bang Bead",
        short_name="bangbead",
    )
    app_configs_list.append(app_configs)

    app_configs = game_app_configs(
        long_name="Blue's Journey",
        short_name="bjourney",
    )
    app_configs_list.append(app_configs)

    app_configs = game_app_configs(
        long_name="Blazing Star",
        short_name="blazstar",
    )
    app_configs_list.append(app_configs)

    app_configs = game_app_configs(
        long_name="Breakers",
        short_name="breakers",
    )
    app_configs_list.append(app_configs)

    app_configs = game_app_configs(
        long_name="Breakers Revenge",
        short_name="breakrev",
    )
    app_configs_list.append(app_configs)

    app_configs = game_app_configs(
        long_name="Baseball Stars Professional",
        short_name="bstars",
    )
    app_configs_list.append(app_configs)

    app_configs = game_app_configs(
        long_name="Baseball Stars 2",
        short_name="bstars2",
    )
    app_configs_list.append(app_configs)

    app_configs = game_app_configs(
        long_name="Burning Fight",
        short_name="burningf",
    )
    app_configs_list.append(app_configs)

    app_configs = game_app_configs(
        long_name="Battle Flip Shot",
        short_name="flipshot",
    )
    app_configs_list.append(app_configs)

    app_configs = game_app_configs(
        long_name="Magical Drop II",
        short_name="magdrop2",
    )
    app_configs_list.append(app_configs)

    app_configs = game_app_configs(
        long_name="Magical Drop III",
        short_name="magdrop3",
    )
    app_configs_list.append(app_configs)

    app_configs = game_app_configs(
        long_name="Magician Lord",
        short_name="maglord",
    )
    app_configs_list.append(app_configs)

    app_configs = game_app_configs(
        long_name="Mahjong 2",
        short_name="mahretsu",
    )
    app_configs_list.append(app_configs)

    app_configs = game_app_configs(
        long_name="Money Puzzle Exchanger",
        short_name="miexchng",
    )
    app_configs_list.append(app_configs)

    app_configs = game_app_configs(
        long_name="Mahjong 1",
        short_name="minasan",
    )
    app_configs_list.append(app_configs)

    app_configs = game_app_configs(
        long_name="Metal Slug",
        short_name="mslug",
    )
    app_configs_list.append(app_configs)

    app_configs = game_app_configs(
        long_name="Metal Slug 2",
        short_name="mslug2",
    )
    app_configs_list.append(app_configs)

    app_configs = game_app_configs(
        long_name="Mutation Nation",
        short_name="mutnat",
    )
    app_configs_list.append(app_configs)

    while True:
        export_to_dir = LocalConfigs.export_to_directory()
        print(f"\n默认目标文件夹路径：{export_to_dir}")
        user_input = input("请目标文件夹路径，使用默认路径请直接按回车 > ")
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
