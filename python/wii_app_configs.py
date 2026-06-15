# -- coding: UTF-8 --

from local_configs import LocalConfigs
from pathlib import Path
from wiiflow_game import WiiFlow_Game
from wiiflow_games_db import WiiFlow_GamesDB
from wiiflow_rom import WiiFlow_Rom


class Wii_AppConfigs:
    DEVICE_SD = "sd"
    DEVICE_USB = "usb"

    default_short_description = None

    def __init__(
        self, app_name: str, app_folder_base_name: str, rom: WiiFlow_Rom, remap=None
    ):
        self.app_name = app_name
        self.app_folder_base_name = app_folder_base_name
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
        self.use_favorites_as_playlist = False

    def set_short_description(self, short_description):
        self._short_description = short_description

    def short_description(self) -> str:
        if self._short_description is None:
            return Wii_AppConfigs.default_short_description
        else:
            return self._short_description
