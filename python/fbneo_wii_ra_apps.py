# -- coding: UTF-8 --

from init_global_configs import Init_Global_Configs
from local_configs import LocalConfigs
from pathlib import Path
from wii_ra_app import WiiRA_App
from wii_ra_app_configs import WiiRA_AppConfigs
from wii_ra_configs import WiiRA_Configs
from wii_ra_ss_app import WiiRA_SS_App
from wii_ra_ss_app_configs import WiiRA_SS_AppConfigs
from wiiflow_configs import WiiFlow_Configs
from wiiflow_game import WiiFlow_Game
from wiiflow_games_db import WiiFlow_GamesDB
from wiiflow_rom import WiiFlow_Rom
from wiiflow_roms_db import WiiFlow_RomsDB


if __name__ == "__main__":
    Init_Global_Configs()

    ss_app_configs = WiiRA_SS_AppConfigs(
        app_name="RA-SS FBNeo",
        folder_name="ra-fbneo",
    )
    ss_app_configs.long_description = (
        "- Mod By RunningSnakes.\n"
        "- Emulator for arcade games based on RA-SS Hexaeco."
    )

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

            ss_app_configs.device = device
            WiiRA_SS_App(ss_app_configs).export_all()
        except ValueError:
            break
