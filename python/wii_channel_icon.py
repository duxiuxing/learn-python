# -- coding: UTF-8 --

from game import Game
from games_db import GamesDB
from helper import Helper
from local_configs import LocalConfigs
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

    # 优先使用 res 文件夹里的 logo.png，如果没有则使用 media\logo 文件夹里的
    def load_logo(self):
        logo_png_path = self.res_directory().joinpath("logo.png")
        if not logo_png_path.exists() or not logo_png_path.is_file():
            rom = WiiFlow_RomsDB.query_rom(rom_file_title=self.rom_file_title)
            game = GamesDB.query_game(game_id=rom.game_id)
            logo_png_path = ResourceFileHelper.compute_game_media_file_path(
                game, "logo", ".png"
            )
        return Image.open(logo_png_path)

    @staticmethod
    def check_logo_left(logo, pixel_test):
        for x in range(logo.width):
            for y in range(logo.height):
                if logo.getpixel((x, y)) != pixel_test:
                    return x
        return 0

    @staticmethod
    def check_logo_top(logo, pixel_test):
        for y in range(logo.height):
            for x in range(logo.width):
                if logo.getpixel((x, y)) != pixel_test:
                    return y
        return 0

    @staticmethod
    def check_logo_right(logo, pixel_test):
        for x_offset in range(1, logo.width + 1):
            for y in range(logo.height):
                if logo.getpixel((logo.width - x_offset, y)) != pixel_test:
                    return logo.width - x_offset
        return logo.width - 1

    @staticmethod
    def check_logo_bottom(logo, pixel_test):
        for y_offset in range(1, logo.height + 1):
            for x in range(logo.width):
                if logo.getpixel((x, logo.height - y_offset)) != pixel_test:
                    return logo.height - y_offset
        return logo.height - 1

    def crop_logo(self):
        logo = self.load_logo()
        pixel_test = logo.getpixel((0, 0))

        left = WiiChannel_Icon.check_logo_left(logo, pixel_test)
        top = WiiChannel_Icon.check_logo_top(logo, pixel_test)
        right = WiiChannel_Icon.check_logo_right(logo, pixel_test)
        bottom = WiiChannel_Icon.check_logo_bottom(logo, pixel_test)

        if (
            left == 0
            and top == 0
            and right == logo.width - 1
            and bottom == logo.height - 1
        ):
            return logo

        return logo.crop((left, top, right + 1, bottom + 1))

    def make(self):
        icon_image = Image.open(self.res_directory().joinpath("IconImage-bg.png"))

        logo = self.crop_logo()
        new_height = 80
        top = 8
        new_width = int(logo.width * new_height / logo.height)
        if new_width > 110:
            new_width = 110
        left = int((128 - new_width) / 2)
        new_logo = logo.resize((new_width, new_height))
        icon_image.paste(new_logo, (left, top), mask=new_logo)

        icon_path = self.res_directory().joinpath("IconImage.png")
        if icon_path.exists() and icon_path.is_file():
            icon_path.unlink()
        icon_image.save(icon_path)
