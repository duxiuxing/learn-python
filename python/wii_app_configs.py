# -- coding: UTF-8 --

from local_configs import LocalConfigs
from pathlib import Path
from ra_configs import RA_Configs
from ra_playlist_configs import RA_PlaylistConfigs
from ra_playlist_item import RA_PlaylistItem
from wii_ra_configs import WiiRA_Configs
from wiiflow_configs import WiiFlow_Configs
from wiiflow_game import WiiFlow_Game
from wiiflow_games_db import WiiFlow_GamesDB
from wiiflow_rom import WiiFlow_Rom
from wiiflow_roms_db import WiiFlow_RomsDB

game_app_configs_list = []


class Wii_AppConfigs:
    DEVICE_SD = "sd"
    DEVICE_USB = "usb"

    default_short_description = None

    def __init__(
        self, app_name: str, base_app_folder_name: str, rom: WiiFlow_Rom, remap=None
    ):
        self.app_name = app_name
        self.base_app_folder_name = base_app_folder_name
        self.rom = rom
        self.remap = remap
        self.device = None
        self._short_description = None

        self.long_description = None
        if rom is not None:
            game = WiiFlow_GamesDB.query_game(game_id=rom.game_id)
            game_name = game.name.replace("&", "&amp;")
            if game.developer == game.publisher:
                self.long_description = (
                    f"{game_name}\n\n"
                    f"- Developer &amp; Publisher: {game.developer}\n"
                    f"- Genre: {game.en_genre}\n"
                    f"- Release Date: {game.date}\n"
                    f"- Max Players: {game.players}"
                )
            else:
                self.long_description = (
                    f"{game_name}\n\n"
                    f"- Developer: {game.developer}\n"
                    f"- Publisher: {game.publisher}\n"
                    f"- Genre: {game.en_genre}\n"
                    f"- Release Date: {game.date}\n"
                    f"- Max Players: {game.players}"
                )

        self.cfg_file_name = None
        self.playlist_configs = None
        self.use_favorites_as_playlist = False

    def set_short_description(self, short_description):
        self._short_description = short_description

    def short_description(self) -> str:
        if self._short_description is None:
            return Wii_AppConfigs.default_short_description
        else:
            return self._short_description

    def init_playlist_configs(self):
        game_list = []
        for rom in WiiFlow_RomsDB.all_roms():
            game_list.append(WiiFlow_GamesDB.query_game(game_id=rom.game_id))

        self.playlist_configs = RA_PlaylistConfigs()
        self.playlist_configs.roms_relative_directory = Path(RA_Configs.wii_roms_relative_directory)
        rom_folder_wii_path = WiiRA_Configs.wii_roms_directory(self.device)
        for game in sorted(game_list, key=lambda x: x.name):
            rom = WiiFlow_RomsDB.query_rom(game_id=game.id)
            item = RA_PlaylistItem(
                path=f"{rom_folder_wii_path}/{rom.file_name()}",
                label=game.name,
                crc32=rom.crc32,
                db_name=RA_Configs.lpl_file_name,
            )
            self.playlist_configs.item_list.append(item)


def add_game_app_configs(rom_file_title: str, app_name=None, remap=None):
    rom = WiiFlow_RomsDB.query_rom(rom_file_title=rom_file_title)
    game = WiiFlow_GamesDB.query_game(rom.game_id)
    if app_name is None:
        app_name = game.name
    elif app_name == game.name:
        print(f"【提示】{rom.file_title} App 无需指定 app_name")

    app_configs = Wii_AppConfigs(
        app_name=app_name, base_app_folder_name=rom_file_title, rom=rom, remap=remap
    )
    game_app_configs_list.append(app_configs)
