# -- coding: UTF-8 --

from init_global_configs import Init_Global_Configs
from local_configs import LocalConfigs
from wii_ra_app_configs import WiiRA_AppConfigs
from wii_ra_app import WiiRA_App


if __name__ == "__main__":
    Init_Global_Configs()

    app_configs_list = []
    app_configs = WiiRA_AppConfigs(
        long_name="Capcom - CP System I",
        short_name="cps1",
        rom_file_list=[
            "1941.zip",
            "dino.zip",
            "captcomm.zip",
            "dynwar.zip",
            "ffight.zip",
            "sf2ce.zip",
            "sf2hf.zip",
            "sf2.zip",
            "sfzch.zip",
            "punisher.zip",
            "3wonders.zip",
            "wof.zip",
        ],
    )
    app_configs.long_description = (
        "- Emulator for CPS-1 games based on RetroArch.\n"
        "- Based on a snapshot of the FB Alpha codebase from 2012.\n"
        "- Compatible with FB Alpha v0.2.97.29 ROM sets."
    )
    app_configs_list.append(app_configs)

    app_configs = WiiRA_AppConfigs(
        long_name="1941 - Counter Attack",
        short_name="1941",
        rom_file_list=["1941.zip"],
    )
    app_configs_list.append(app_configs)

    app_configs = WiiRA_AppConfigs(
        long_name="Cadillacs and Dinosaurs",
        short_name="dino",
        rom_file_list=["dino.zip"],
    )
    app_configs_list.append(app_configs)

    app_configs = WiiRA_AppConfigs(
        long_name="Captain Commando",
        short_name="captcomm",
        rom_file_list=["captcomm.zip"],
    )
    app_configs_list.append(app_configs)

    app_configs = WiiRA_AppConfigs(
        long_name="Dynasty Wars",
        short_name="dynwar",
        rom_file_list=["dynwar.zip"],
    )
    app_configs_list.append(app_configs)

    app_configs = WiiRA_AppConfigs(
        long_name="Final Fight",
        short_name="ffight",
        rom_file_list=["ffight.zip"],
    )
    app_configs_list.append(app_configs)

    app_configs = WiiRA_AppConfigs(
        long_name="Street Fighter 2' CE",
        short_name="sf2ce",
        rom_file_list=["sf2ce.zip"],
    )
    app_configs_list.append(app_configs)

    app_configs = WiiRA_AppConfigs(
        long_name="The Punisher",
        short_name="punisher",
        rom_file_list=["punisher.zip"],
    )
    app_configs_list.append(app_configs)

    app_configs = WiiRA_AppConfigs(
        long_name="Three Wonders",
        short_name="3wonders",
        rom_file_list=["3wonders.zip"],
    )
    app_configs_list.append(app_configs)

    app_configs = WiiRA_AppConfigs(
        long_name="Warriors of Fate",
        short_name="wof",
        rom_file_list=["wof.zip"],
    )
    app_configs_list.append(app_configs)

    while True:
        print(f"\n输出 Wii App 到 {LocalConfigs.export_to_directory()}")
        print("1. 输出 USB App")
        print("2. 输出 SD App")
        print("其他输入表示退出")
        user_input = input("请输入操作的序号：")
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
