# -- coding: UTF-8 --

from wii_app_configs import Wii_AppConfigs
from wiiflow_game import WiiFlow_Game
from wiiflow_games_db import WiiFlow_GamesDB
from wiiflow_rom import WiiFlow_Rom
from wiiflow_roms_db import WiiFlow_RomsDB


class Wii_AppFactory:
    game_app_configs_list = []

    @staticmethod
    def add_game_app_configs(
        rom_file_title: str, app_name: str | None = None, remap: str | None = None
    ):
        rom = WiiFlow_RomsDB.query_rom(rom_file_title=rom_file_title)
        game = WiiFlow_GamesDB.query_game(rom.game_id)
        if app_name is None:
            app_name = game.name
        elif app_name == game.name:
            print(f"【提示】{rom.file_title} App 无需指定 app_name")

        app_configs = Wii_AppConfigs(
            app_name=app_name, app_folder_base_name=rom_file_title, rom=rom, remap=remap
        )
        Wii_AppFactory.game_app_configs_list.append(app_configs)
