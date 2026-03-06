# -- coding: UTF-8 --

import os

from helper import Helper
from init_global_configs import Init_Global_Configs
from resource_file_helper import ResourceFileHelper
from game import Game
from games_db import GamesDB
from rom import Rom
from roms_db import RomsDB
from wiiflow_game import WiiFlow_Game
from wiiflow_games_db import WiiFlow_GamesDB
from wiiflow_rom import WiiFlow_Rom
from wiiflow_roms_db import WiiFlow_RomsDB


def check_game_element():
    games = GamesDB.all_games()
    print(f"在 roms.xml 中发现 {len(games)} 个游戏")
    for game in games:
        wiiflow_game = WiiFlow_GamesDB.query_game(game_id=game.id)
        if wiiflow_game is None:
            print(
                "【错误】roms.xml 中的游戏没有在 WiiFlow 中配置\n"
                f"\ten_title = {game.en_title}，id = {game.id}"
            )
        else:
            if game.en_title != wiiflow_game.en_title:
                print(
                    "【错误】en_title 不一致\n"
                    f"\troms.xml: {game.en_title}\n"
                    f"\tWiiFlow: {wiiflow_game.en_title}"
                )

            if game.zhcn_title != wiiflow_game.zhcn_title:
                print(
                    "zhcn_title 不一致\n"
                    f"\troms.xml: {game.zhcn_title}\n"
                    f"\tWiiFlow: {wiiflow_game.zhcn_title}"
                )


def check_rom_element():
    roms = RomsDB.all_roms()
    print(f"在 roms.xml 中发现 {len(roms)} 个 ROM 文件")
    for rom in roms:
        rom_file_path = ResourceFileHelper.compute_rom_file_path(
            rom, include_crc32=True
        )
        rom_file_exists = rom_file_path.exists()

        if not rom_file_exists:
            rom_file_path = ResourceFileHelper.compute_rom_file_path(
                rom, include_crc32=False
            )
            rom_file_exists = rom_file_path.exists()

        if rom_file_exists:
            rom_crc32 = Helper.compute_crc32(rom_file_path)
            if rom_crc32 != rom.crc32:
                print(
                    f"【错误】{rom.file_name} 的 crc32 校验失败\n"
                    f"\t实际值 = {rom_crc32}，预期值 = {rom.crc32}"
                )

            rom_bytes = str(os.stat(rom_file_path).st_size)
            if rom_bytes != rom.bytes:
                print(
                    f"【错误】{rom.file_name} 的 bytes 校验失败\n"
                    f"\t实际值 = {rom_bytes}，预期值 = {rom.bytes}"
                )
        else:
            print(f"【错误】缺失 ROM 文件 {rom_file_path}")


if __name__ == "__main__":
    Init_Global_Configs()

    check_game_element()
    check_rom_element()
