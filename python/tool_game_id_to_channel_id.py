# -- coding: UTF-8 --

from helper import Helper
from init_global_configs import Init_Global_Configs
from wiiflow_rom import WiiFlow_Rom
from wiiflow_roms_db import WiiFlow_RomsDB


if __name__ == "__main__":
    Init_Global_Configs()

    for rom in WiiFlow_RomsDB.all_roms():
        print(f"{rom.file_title} = " + Helper.game_id_to_channel_id(rom.game_id))
