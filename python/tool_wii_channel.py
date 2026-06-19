# -- coding: UTF-8 --

from helper import Helper
from init_global_configs import Init_Global_Configs
from wiiflow_configs import WiiFlow_Configs
from wiiflow_rom import WiiFlow_Rom
from wiiflow_roms_db import WiiFlow_RomsDB

if __name__ == "__main__":
    Init_Global_Configs()

    plugin_name = WiiFlow_Configs.plugin_name.lower()

    channel_id_to_rom_file_title = {}
    all_roms = WiiFlow_RomsDB.all_roms()
    for rom in all_roms:
        channel_id = Helper.game_id_to_channel_id(rom.game_id)
        print(f"{rom.file_title} = " + channel_id)
        if channel_id in channel_id_to_rom_file_title.keys():
            print(
                f"【错误】{channel_id} 已经被 {channel_id_to_rom_file_title[channel_id]} 占用"
            )
        else:
            channel_id_to_rom_file_title[channel_id] = rom.file_title

        print(
            f"apps/sd-{plugin_name}-{rom.file_title}/boot.dol\n"
            f"apps/sd-{plugin_name}-{rom.file_title}-ss/boot.dol\n"
            f"apps/usb-{plugin_name}-{rom.file_title}/boot.dol\n"
            f"apps/usb-{plugin_name}-{rom.file_title}-ss/boot.dol\n"
            f"boot-{plugin_name}-{rom.file_title}\n"
        )

    if len(channel_id_to_rom_file_title) != len(all_roms):
        print("【错误】发现重复的 channel_id")
