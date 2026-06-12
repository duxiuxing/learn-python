# -- coding: UTF-8 --

from helper import Helper
from init_global_configs import Init_Global_Configs
from wiiflow_configs import WiiFlow_Configs
from wiiflow_rom import WiiFlow_Rom
from wiiflow_roms_db import WiiFlow_RomsDB

if __name__ == "__main__":
    Init_Global_Configs()

    plugin_name = WiiFlow_Configs.plugin_name.lower()

    for rom in WiiFlow_RomsDB.all_roms():
        print(f"{rom.file_title} = " + Helper.game_id_to_channel_id(rom.game_id))

        print(
            f"apps/sd-{plugin_name}-{rom.file_title}/boot.dol\n"
            f"apps/sd-{plugin_name}-{rom.file_title}-ss/boot.dol\n"
            f"apps/usb-{plugin_name}-{rom.file_title}/boot.dol\n"
            f"apps/usb-{plugin_name}-{rom.file_title}-ss/boot.dol\n"
        )
