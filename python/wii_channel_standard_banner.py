# -- coding: UTF-8 --

from game import Game
from games_db import GamesDB
from helper import Helper
from local_configs import LocalConfigs
from PIL import Image
from resource_file_helper import ResourceFileHelper
from wii_channel_icon import WiiChannel_Icon
from wiiflow_rom import WiiFlow_Rom
from wiiflow_roms_db import WiiFlow_RomsDB

standard_banner_configs_list = []


class StandardBannerConfigs:
    COMPANY_LOGO_WIDTH = 142
    COMPANY_LOGO_HEIGHT = 29
    COMPANY_LOGO_OFFSET_X_TOP = 34
    COMPANY_LOGO_OFFSET_X_BOTTOM = 6
    COMPANY_LOGO_OFFSET_Y = 8
    COMPANY_LOGO_ALIGN_LEFT_TOP = (34, 8)
    COMPANY_LOGO_ALIGN_LEFT_BOTTOM = (6, 297)

    # 414 = MENU_SCREEN_WIDTH - COMPANY_LOGO_WIDTH - COMPANY_LOGO_OFFSET_X_TOP
    COMPANY_LOGO_ALIGN_RIGHT_TOP = (414, 8)

    # 442 = MENU_SCREEN_WIDTH - COMPANY_LOGO_WIDTH - COMPANY_LOGO_OFFSET_X_BOTTOM
    COMPANY_LOGO_ALIGN_RIGHT_BOTTOM = (442, 297)

    # 224 = (MENU_SCREEN_WIDTH - COMPANY_LOGO_WIDTH) / 2
    COMPANY_LOGO_ALIGN_TOP_CENTER = (224, 8)
    COMPANY_LOGO_ALIGN_BOTTOM_CENTER = (224, 297)

    MENU_SCREEN_WIDTH = 590
    MENU_SCREEN_HEIGHT = 332

    def __init__(
        self,
        rom_file_title,
        game_logo_size=None,
        game_logo_left_top=None,
        company_logo_left_top=None,
        index=None,
    ):
        self.rom_file_title = rom_file_title
        self.game_logo_size = game_logo_size
        self.game_logo_left_top = game_logo_left_top
        self.company_logo_left_top = company_logo_left_top
        self.index = index


class StandardBanner:
    def __init__(self, banner_configs: StandardBannerConfigs):
        self.configs = banner_configs

    def res_directory(self):
        return LocalConfigs.repository_directory.joinpath(
            f"wii\\wad\\{self.configs.rom_file_title}\\res",
        )

    def standard_directory(self):
        if self.configs.index is None:
            return self.res_directory().joinpath(
                "standard",
            )
        else:
            return self.res_directory().joinpath(
                f"standard-{self.configs.index}",
            )

    def load_main_screen_bg(self):
        main_screen_bg_path = self.standard_directory().joinpath(
            "MenuScreen1-bg.png",
        )
        if main_screen_bg_path.exists() and main_screen_bg_path.is_file():
            return Image.open(main_screen_bg_path)
        else:
            rom = WiiFlow_RomsDB.query_rom(rom_file_title=self.configs.rom_file_title)
            game = GamesDB.query_game(game_id=rom.game_id)
            wallpaper_path = ResourceFileHelper.compute_game_media_file_path(
                game, "wallpaper", ".jpg"
            )
            image = Image.open(wallpaper_path).resize(
                (
                    StandardBannerConfigs.MENU_SCREEN_WIDTH,
                    StandardBannerConfigs.MENU_SCREEN_HEIGHT,
                )
            )
            Helper.verify_exist_directory_ex(self.standard_directory())
            image.save(main_screen_bg_path, format="PNG")
            return image

    def make(self):
        main_screen_bg = self.load_main_screen_bg()

        if self.configs.game_logo_size is not None:
            logo_png_path = self.standard_directory().joinpath("logo.png")
            if not logo_png_path.exists() or not logo_png_path.is_file():
                logo_png_path = None
            game_logo = (
                WiiChannel_Icon(self.configs.rom_file_title, logo_png_path)
                .load_logo()
                .resize(self.configs.game_logo_size)
            )
            main_screen_bg.paste(
                game_logo, self.configs.game_logo_left_top, mask=game_logo
            )

        if self.configs.company_logo_left_top is not None:
            company_logo_path = LocalConfigs.repository_directory.joinpath(
                "wii\\wad\\company-logo.png",
            )
            company_logo = Image.open(company_logo_path)
            main_screen_bg.paste(
                company_logo, self.configs.company_logo_left_top, mask=company_logo
            )

        main_screen1_path = self.standard_directory().joinpath("MenuScreen1.png")
        if main_screen1_path.exists() and main_screen1_path.is_file():
            main_screen1_path.unlink()
        main_screen_bg.save(main_screen1_path)
