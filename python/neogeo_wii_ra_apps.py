# -- coding: UTF-8 --

from init_global_configs import Init_Global_Configs
from local_configs import LocalConfigs
from wii_ra_app_configs import WiiRA_AppConfigs
from wii_ra_app import WiiRA_App


if __name__ == "__main__":
    Init_Global_Configs()

    app_configs_list = []
    app_configs = WiiRA_AppConfigs(
        long_name="SNK - Neo Geo",
        short_name="neogeo",
        rom_file_list=[
            "sonicwi2.zip",
            "sonicwi3.zip",
        ],
    )
    app_configs.long_description = (
        "- Emulator for Neo Geo games based on RetroArch.\n"
        "- Based on a snapshot of the FB Alpha codebase from circa 2012.\n"
        "- Compatible with FB Alpha v0.2.97.29 ROM sets."
    )
    # app_configs_list.append(app_configs)

    app_configs = WiiRA_AppConfigs(
        long_name="Aero Fighters 2",
        short_name="sonicwi2",
        rom_file_list=["sonicwi2.zip"],
    )
    app_configs_list.append(app_configs)

    app_configs = WiiRA_AppConfigs(
        long_name="Aero Fighters 3",
        short_name="sonicwi3",
        rom_file_list=["sonicwi3.zip"],
    )
    app_configs_list.append(app_configs)

    app_configs = WiiRA_AppConfigs(
        long_name="Alpha Mission II",
        short_name="alpham2",
        rom_file_list=["alpham2.zip"],
    )
    app_configs_list.append(app_configs)

    app_configs = WiiRA_AppConfigs(
        long_name="Art of Fighting",
        short_name="aof",
        rom_file_list=["aof.zip"],
    )
    app_configs_list.append(app_configs)

    app_configs = WiiRA_AppConfigs(
        long_name="Art of Fighting 2",
        short_name="aof2",
        rom_file_list=["aof2.zip"],
    )
    app_configs_list.append(app_configs)

    app_configs = WiiRA_AppConfigs(
        long_name="Art of Fighting 3",
        short_name="aof3",
        rom_file_list=["aof3.zip"],
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
