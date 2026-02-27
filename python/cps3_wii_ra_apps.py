# -- coding: UTF-8 --

from init_global_configs import Init_Global_Configs
from local_configs import LocalConfigs
from wii_ra_app_configs import WiiRA_AppConfigs
from wii_ra_app import WiiRA_App


if __name__ == "__main__":
    Init_Global_Configs()

    app_configs_list = []
    app_configs = WiiRA_AppConfigs(
        long_name="Capcom - CP System III",
        short_name="cps3",
        rom_file_list=[
            "jojoba.zip",
            "jojo.zip",
            "redearth.zip",
            "sfiii.zip",
            "sfiii2.zip",
            "sfiii3.zip",
        ],
    )
    app_configs.long_description = (
        "- Emulator for CPS-3 games based on RetroArch.\n"
        "- Based on a snapshot of the FB Alpha codebase from 2012.\n"
        "- Compatible with FB Alpha v0.2.97.29 ROM sets."
    )
    app_configs_list.append(app_configs)

    app_configs = WiiRA_AppConfigs(
        long_name="JoJo's Venture 2",
        short_name="jojoba",
        rom_file_list=["jojoba.zip"],
    )
    app_configs_list.append(app_configs)

    app_configs = WiiRA_AppConfigs(
        long_name="JoJo's Venture",
        short_name="jojo",
        rom_file_list=["jojo.zip"],
    )
    app_configs_list.append(app_configs)

    app_configs = WiiRA_AppConfigs(
        long_name="Red Earth",
        short_name="redearth",
        rom_file_list=["redearth.zip"],
    )
    app_configs_list.append(app_configs)

    app_configs = WiiRA_AppConfigs(
        long_name="Street Fighter 3.1",
        short_name="sfiii",
        rom_file_list=["sfiii.zip"],
    )
    app_configs_list.append(app_configs)

    app_configs = WiiRA_AppConfigs(
        long_name="Street Fighter 3.2",
        short_name="sfiii2",
        rom_file_list=["sfiii2.zip"],
    )
    app_configs_list.append(app_configs)

    app_configs = WiiRA_AppConfigs(
        long_name="Street Fighter 3.3",
        short_name="sfiii3",
        rom_file_list=["sfiii3.zip"],
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
