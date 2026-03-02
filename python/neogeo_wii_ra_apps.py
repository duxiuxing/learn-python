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
        "sonicwi2.zip",
        "sonicwi3.zip",
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
        "- Emulator for Neo Geo games based on RetroArch.\n"
        "- Based on a snapshot of the FB Alpha codebase from circa 2012.\n"
        "- Compatible with FB Alpha v0.2.97.29 ROM sets."
    )
    # app_configs_list.append(app_configs)

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
        long_name="Alpha Mission II",
        short_name="alpham2",
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

    while True:
        print(f"\n输出 Wii App 到 {LocalConfigs.export_to_directory()}")
        print("1. 输出 USB App")
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
