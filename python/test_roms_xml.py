# -- coding: UTF-8 --

import os

from game import Game
from games_db import GamesDB
from helper import Helper
from init_global_configs import Init_Global_Configs
from resource_file_helper import ResourceFileHelper
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
                "【错误】roms.xml 中的 <Game> 没有在 WiiFlow 中配置："
                f"id = {game.id}，en_title = {game.en_title}"
            )
        else:
            en_title_match = True
            if game.en_title != wiiflow_game.en_title:
                en_title_match = False

            zhcn_title_match = True
            if game.zhcn_title != wiiflow_game.zhcn_title:
                zhcn_title_match = False

            if en_title_match and zhcn_title_match:
                print(f"roms.xml 中的 <Game> 匹配：{game.en_title}，{game.zhcn_title}")
            else:
                en_title_msg = ""
                if en_title_match is False:
                    en_title_msg = f"\n\ten_title 不一致\n\t\troms.xml: {game.en_title}\n\t\tWiiFlow: {wiiflow_game.en_title}"

                zhcn_title_msg = ""
                if zhcn_title_match is False:
                    zhcn_title_msg = f"\n\tzhcn_title 不一致\n\t\troms.xml: {game.zhcn_title}\n\t\tWiiFlow: {wiiflow_game.zhcn_title}"

                print(
                    f"【错误】roms.xml 中的 <Game> 不匹配：id = {game.id}{en_title_msg}{zhcn_title_msg}"
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
            rom_crc32_match = rom_crc32 == rom.crc32

            rom_bytes = str(os.stat(rom_file_path).st_size)
            rom_bytes_match = rom_bytes == rom.bytes

            if rom_crc32_match and rom_bytes_match:
                continue
            else:
                rom_crc32_msg = ""
                if rom_crc32_match is False:
                    rom_crc32_msg = f"\n\tcrc32 不匹配\n\t\t实际值 = {rom_crc32}，预期值 = {rom.crc32}"

                rom_bytes_msg = ""
                if rom_bytes_match is False:
                    rom_bytes_msg = f"\n\tbytes 不匹配\n\t\t实际值 = {rom_bytes}，预期值 = {rom.bytes}"

                print(
                    f"【错误】roms.xml 中的 <Rom> 校验失败：file_name = {rom.file_name}{rom_crc32_msg}{rom_bytes_msg}"
                )
        else:
            print(f"【错误】缺失 ROM 文件 {rom_file_path}")


if __name__ == "__main__":
    Init_Global_Configs()

    check_game_element()
    check_rom_element()
