# -- coding: UTF-8 --

import json
import os

from game import Game
from games_db import GamesDB
from helper import Helper
from local_configs import LocalConfigs
from pathlib import Path
from ra_resource_file_helper import RA_ResourceFileHelper
from ra_rom import RA_Rom
from resource_file_helper import ResourceFileHelper
from rom import Rom
from roms_db import RomsDB
from roms_xml import RomsXML
from wiiflow_games_db import WiiFlow_GamesDB
from wiiflow_plugins_data import WiiFlowPluginsData
from wiiflow_rom import WiiFlow_Rom
from wiiflow_roms_db import WiiFlow_RomsDB


class RA_PlaylistImport:
    @staticmethod
    def parse(playlist_name: str):
        ra_import = RA_PlaylistImport(playlist_name)

        lpl_file_path = LocalConfigs.retroarch_directory().joinpath(
            f"playlists\\{playlist_name}.lpl"
        )
        with open(lpl_file_path, "r", encoding="utf-8") as file:
            items = json.load(file)["items"]
            for item in items:
                ra_rom = RA_Rom(
                    file_path=Path(item["path"]),
                    label=item["label"],
                    crc32=item["crc32"].split("|")[0],
                    playlist_name=Path(item["db_name"]).name,
                )
                game = ra_import._verify_game_in_games_db(ra_rom)
                ra_import._try_rom_file(ra_rom, game)


    def __init__(self, playlist_name: str):
        self.playlist_name = playlist_name

    def _verify_game_in_games_db(self, ra_rom: RA_Rom):
        rom = RomsDB.query_rom(
            rom_crc32=ra_rom.crc32, rom_file_name=ra_rom.file_path.name
        )
        if rom is not None:
            return GamesDB.query_game(game_id=rom.game_id)

        wiiflow_rom = WiiFlow_RomsDB.query_rom(
            rom_crc32=ra_rom.crc32, rom_file_title=ra_rom.file_path.stem
        )
        if wiiflow_rom is not None:
            wiiflow_game = WiiFlow_GamesDB.query_game(game_id=wiiflow_rom.game_id)
            game = GamesDB.query_game(game_id=wiiflow_game.id)
            if game is None:
                game = Game(
                    id=wiiflow_game.id,
                    en_title=wiiflow_game.en_title,
                    zhcn_title=wiiflow_game.zhcn_title,
                )
                GamesDB.add_game(game)
            return game

        game_title = Helper.remove_region(ra_rom.label)
        game = GamesDB.query_game(game_title=game_title)
        if game is not None:
            return game.en_title

        wiiflow_game = WiiFlow_GamesDB.query_game(game_title=game_title)
        if wiiflow_game is not None:
            game = GamesDB.query_game(game_title=wiiflow_game.en_title)
            if game is None:
                game = Game(
                    id=wiiflow_game.id,
                    en_title=wiiflow_game.en_title,
                    zhcn_title=wiiflow_game.zhcn_title,
                )
                GamesDB.add_game(game)
            return game

        show_tips = True
        while show_tips:
            print(
                f"发现新游戏的 ROM 文件：{ra_rom.file_path.name}，请输入新游戏的英文名称"
            )
            game_title_input = input(
                f"直接按回车则使用“{game_title}”作为新游戏的英文名称 > "
            )
            if len(game_title_input) > 0:
                game_title = game_title_input
            else:
                show_tips = False

        game = GamesDB.query_game(game_title=game_title)
        if game is None:
            wiiflow_game = WiiFlow_GamesDB.query_game(game_title=game_title)
            if wiiflow_game is None:
                game = Game(
                    id=GamesDB.new_id(),
                    en_title=game_title,
                    zhcn_title=game_title,
                )
            else:
                game = Game(
                    id=wiiflow_game.id,
                    en_title=wiiflow_game.en_title,
                    zhcn_title=wiiflow_game.zhcn_title,
                )
            GamesDB.add_game(game)
        return game

    @staticmethod
    def _query_game(ra_rom: RA_Rom):
        rom = RomsDB.query_rom(rom_crc32=ra_rom.crc32, rom_file_name=ra_rom.file_name)
        if rom is None:
            en_title = Helper.remove_region(ra_rom.label)
            game = GamesDB.query_game(game_title=en_title)
            if game is None:
                game = Game(id=GamesDB.new_id(), en_title=en_title, zhcn_title=None)
                GamesDB.add_game(game)
            return game
        else:
            return GamesDB.query_game(game_id=rom.game_id)

    def _try_rom_file(self, ra_rom: RA_Rom, game: Game):
        for rom in game.rom_list:
            if rom.crc32 == ra_rom.crc32:
                return rom
        
        rom = Rom(
            game_id=game.id,
            crc32=ra_rom.crc32,
            bytes=str(os.stat(ra_rom.file_path).st_size),
            file_name=ra_rom.file_path.name,
            parent_rom=None,
            en_title=ra_rom.label,
            zhcn_title=ra_rom.label,
        )
        RomsDB.add_rom(rom)
        dst_rom_file_path = ResourceFileHelper.compute_rom_file_path(rom, include_crc32=False)
        if dst_rom_file_path.exists():
            dst_rom_file_path = ResourceFileHelper.compute_rom_file_path(rom, include_crc32=True)

        Helper.copy_file_if_not_exist(ra_rom.file_path, dst_rom_file_path)
        return rom

    def _try_thumbnail_file(self, ra_rom: RA_Rom, game: Game, src_folder_name, dst_folder_name):
        src_file_path = RA_ResourceFileHelper.compute_game_media_file_path(ra_rom, src_folder_name, ".png")
        dst_file_path = ResourceFileHelper.compute_game_media_file_path(game, dst_folder_name, ".png")



if __name__ == "__main__":
    RomsXML.load()
    WiiFlowPluginsData.load()

    RA_PlaylistImport.parse("FBNeo - Arcade Games")
