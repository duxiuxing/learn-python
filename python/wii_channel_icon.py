# -- coding: UTF-8 --
import os

from game import Game
from games_db import GamesDB
from helper import Helper
from local_configs import LocalConfigs
from logo import Logo
from pathlib import Path
from PIL import Image
from resource_file_helper import ResourceFileHelper
from wiiflow_rom import WiiFlow_Rom
from wiiflow_roms_db import WiiFlow_RomsDB

rom_file_title_list = []


class WiiChannel_Icon:
    def __init__(self, rom_file_title):
        self.rom_file_title = rom_file_title

    def res_directory(self):
        return LocalConfigs.repository_directory.joinpath(
            f"wii\\wad\\{self.rom_file_title}\\res",
        )

    def game_logo_path(self, root_dir: Path) -> Path:
        logo_png_path = root_dir.joinpath("logo.png")
        if not logo_png_path.exists() or not logo_png_path.is_file():
            logo_png_path = self.res_directory().joinpath("logo.png")
            if not logo_png_path.exists() or not logo_png_path.is_file():
                rom = WiiFlow_RomsDB.query_rom(rom_file_title=self.rom_file_title)
                game = GamesDB.query_game(game_id=rom.game_id)
                logo_png_path = ResourceFileHelper.compute_game_media_file_path(
                    game, "logo", ".png"
                )
        return logo_png_path

    def make_image_if_bg_file_exist(self, root_dir: Path):
        bg_file_path = root_dir.joinpath("IconImage-bg.png")
        if not bg_file_path.exists() or not bg_file_path.is_file():
            return

        logo = Logo.resize(
            self.game_logo_path(root_dir),
            max_width=110,
            max_height=80,
            min_height=62,
        )
        dst_png = Image.open(bg_file_path)
        x_offset = int((dst_png.width - logo.width) / 2)
        y_offset = int((dst_png.height - logo.height) / 2)
        dst_png.paste(logo, (x_offset, y_offset), mask=logo)

        dst_png_file_path = root_dir.joinpath("IconImage.png")
        if dst_png_file_path.exists() and dst_png_file_path.is_file():
            dst_png_file_path.unlink()
        dst_png.save(dst_png_file_path)

    def make(self):
        self.make_image_if_bg_file_exist(self.res_directory())

        for folder_name in os.listdir(self.res_directory()):
            dir = self.res_directory().joinpath(folder_name)
            if dir.is_dir():
                self.make_image_if_bg_file_exist(dir)
