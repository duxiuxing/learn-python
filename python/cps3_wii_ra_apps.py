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
        "jojoba.zip",
        "jojo.zip",
        "redearth.zip",
        "sfiii.zip",
        "sfiii2.zip",
        "sfiii3.zip",
    ]
    rom_file_path_list = []
    for rom_file_name in rom_file_list:
        rom_file_path = Path("games").joinpath(
            WiiFlow_Configs.plugin_name().lower(),
            rom_file_name,
        )
        rom_file_path_list.append(rom_file_path)
    app_configs = WiiRA_AppConfigs(
        long_name="Capcom - CP System III",
        short_name="cps3",
        rom_file_path_list=rom_file_path_list,
    )
    app_configs.long_description = (
        "- Emulator for CPS-3 games based on RetroArch.\n"
        "- Based on a snapshot of the FB Alpha codebase from 2012.\n"
        "- Compatible with FB Alpha v0.2.97.29 ROM sets."
    )
    app_configs_list.append(app_configs)

    app_configs = game_app_configs(
        long_name="JoJo's Venture 2",
        short_name="jojoba",
    )
    app_configs_list.append(app_configs)

    app_configs = game_app_configs(
        long_name="JoJo's Venture",
        short_name="jojo",
    )
    app_configs_list.append(app_configs)

    app_configs = game_app_configs(
        long_name="Red Earth",
        short_name="redearth",
    )
    app_configs_list.append(app_configs)

    app_configs = game_app_configs(
        long_name="Street Fighter 3.1",
        short_name="sfiii",
    )
    app_configs_list.append(app_configs)

    app_configs = game_app_configs(
        long_name="Street Fighter 3.2",
        short_name="sfiii2",
    )
    app_configs_list.append(app_configs)

    app_configs = game_app_configs(
        long_name="Street Fighter 3.3",
        short_name="sfiii3",
    )
    app_configs_list.append(app_configs)

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
