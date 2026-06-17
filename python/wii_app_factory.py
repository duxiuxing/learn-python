# -- coding: UTF-8 --

from ra_playlist_configs import RA_PlaylistConfigs
from wii_app_configs import Wii_AppConfigs
from wii_ra_app import WiiRA_App
from wii_ra_configs import WiiRA_Configs
from wii_ra_vm_app import WiiRA_VM_App
from wii_ss_app import WiiSS_App
from wii_ss_configs import WiiSS_Configs
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

    @staticmethod
    def export_game_ra_apps(wii_device: str):
        for app_configs in Wii_AppFactory.game_app_configs_list:
            app_configs.device = wii_device
            ra_app = WiiRA_App(app_configs).export_all()

    @staticmethod
    def export_game_ra_vm_apps(wii_device: str):
        for app_configs in Wii_AppFactory.game_app_configs_list:
            app_configs.cfg_file_name = (
                f"{app_configs.rom.file_title.ljust(9, '_')}.cfg"
            )
            app_configs.device = wii_device
            playlist_configs = WiiRA_VM_App.init_playlist_configs(
                rom_file_title_list=[app_configs.rom.file_title], wii_device=wii_device
            )
            playlist_configs.boxarts_folder = None
            playlist_configs.logos_folder = None
            playlist_configs.snaps_folder = None
            playlist_configs.titles_folder = None
            WiiRA_VM_App(app_configs, playlist_configs).export_all()

    @staticmethod
    def export_game_ss_apps(wii_device: str):
        for app_configs in Wii_AppFactory.game_app_configs_list:
            app_configs.cfg_file_name = f"{app_configs.rom.file_title}.cfg"
            app_configs.device = wii_device
            WiiSS_App(app_configs).export_all()

    @staticmethod
    def export_game_ss_vm_apps(wii_device: str):
        WiiSS_Configs.settings_dict["system_directory"] = (
            f"{WiiRA_Configs.wii_data_directory(wii_device)}/system"
        )
        for app_configs in Wii_AppFactory.game_app_configs_list:
            app_configs.cfg_file_name = f"{app_configs.rom.file_title}.cfg"
            app_configs.device = wii_device
            WiiSS_App(app_configs).export_all()
