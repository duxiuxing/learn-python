# -- coding: UTF-8 --

from game import Game
from games_db import GamesDB
from helper import Helper
from local_configs import LocalConfigs
from pathlib import Path
from PIL import Image
from resource_file_helper import ResourceFileHelper
from wii_ra_configs import WiiRA_Configs
from wii_ra_ss_app_configs import WiiRA_SS_AppConfigs
from wii_ra_ss_configs import WiiRA_SS_Configs
from wiiflow_configs import WiiFlow_Configs
from wiiflow_game import WiiFlow_Game
from wiiflow_games_db import WiiFlow_GamesDB
from wiiflow_rom import WiiFlow_Rom
from wiiflow_roms_db import WiiFlow_RomsDB


class WiiRA_SS_App:
    def __init__(self, configs: WiiRA_SS_AppConfigs):
        self.configs = configs

    def app_directory(self):
        return LocalConfigs.export_to_directory().joinpath(
            "apps", f"{self.configs.folder_name}-{self.configs.device}"
        )

    def data_directory(self):
        return LocalConfigs.export_to_directory().joinpath(
            "private", WiiRA_SS_Configs.data_folder_name()
        )

    def export_core_files(self):
        src_file_path = LocalConfigs.repository_directory().joinpath(
            "wii\\apps",
            WiiRA_SS_Configs.core_folder_name(),
            WiiRA_SS_Configs.core_file_name(),
        )
        dst_file_path = self.app_directory().joinpath("boot.dol")
        Helper.copy_file_if_not_exist(src_file_path, dst_file_path)

    def export_icon_png(self):
        game = Game(id=None, en_title=self.configs.app_name, zhcn_title=None)
        src_icon_png_path = ResourceFileHelper.compute_game_media_file_path(
            game, "logo", ".png"
        )
        if not src_icon_png_path.exists():
            rom_file_title = Path(self.configs.rom_file_path_list[0]).stem
            rom = WiiFlow_RomsDB.query_rom(rom_file_title=rom_file_title)
            game = GamesDB.query_game(game_id=rom.game_id)
            src_icon_png_path = ResourceFileHelper.compute_game_media_file_path(
                game, "logo", ".png"
            )
            if not src_icon_png_path.exists():
                print(f"【错误】无效的源文件 {src_icon_png_path}")
                return

        dst_icon_png_path = self.app_directory().joinpath("icon.png")
        if dst_icon_png_path.exists() and dst_icon_png_path.is_file():
            dst_icon_png_path.unlink()

        Image.open(src_icon_png_path).resize((128, 48)).save(dst_icon_png_path)

    def export_meta_xml(self):
        meta_xml_path = self.app_directory().joinpath("meta.xml")
        if meta_xml_path.exists() and meta_xml_path.is_file():
            meta_xml_path.unlink()

        with open(meta_xml_path, "w", encoding="utf-8") as xml_file:
            xml_file.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n')
            xml_file.write('<app version="1">\n')
            app_name = self.configs.app_name.replace("&", "&amp;")
            xml_file.write(f"  <name>{app_name}</name>\n")
            xml_file.write("  <author>SuperrSonic &amp; R-Sam</author>\n")
            xml_file.write(f"  <version>{self.configs.device}</version>\n")
            xml_file.write(
                f"  <release_date>{WiiRA_SS_Configs.release_date()}</release_date>\n"
            )
            xml_file.write(
                f"  <short_description>{self.configs.short_description()}</short_description>\n"
            )
            if self.configs.long_description is None:
                rom_file_title = Path(self.configs.rom_file_path_list[0]).stem
                rom = WiiFlow_RomsDB.query_rom(rom_file_title=rom_file_title)
                game = WiiFlow_GamesDB.query_game(game_id=rom.game_id)

                game_name = game.name.replace("&", "&amp;")
                xml_file.write(f"  <long_description>{game_name}\n\n")

                if game.developer == game.publisher:
                    xml_file.write(f"- Developer &amp; Publisher: {game.developer}\n")
                else:
                    xml_file.write(f"- Developer: {game.developer}\n")
                    xml_file.write(f"- Publisher: {game.publisher}\n")

                xml_file.write(f"- Genre: {game.en_genre}\n")
                xml_file.write(f"- Release Date: {game.date}\n")
                xml_file.write(f"- Max Players: {game.players}\n\n")
            else:
                xml_file.write(
                    f"  <long_description>{self.configs.long_description}\n\n"
                )

            lower_plugin_name = WiiFlow_Configs.plugin_name().lower()
            xml_file.write(
                f"Wii Channel: {self.configs.device}:/wad/{lower_plugin_name}\n"
            )
            xml_file.write(
                f"Website: https://github.com/R-Sam-1980/{lower_plugin_name}</long_description>\n"
            )
            xml_file.write("  <no_ios_reload/>\n")
            xml_file.write("  <ahb_access/>\n")
            xml_file.write("</app>\n")
            xml_file.close()

    def configs_list(self):
        app_dir = f"{self.configs.device}:/apps/{self.configs.folder_name}-{self.configs.device}"
        data_dir = (
            f"{self.configs.device}:/private/{WiiRA_SS_Configs.data_folder_name()}"
        )
        rgui_browser_directory = str(WiiRA_Configs.roms_directory()).replace("\\", "/")

        list_ret = [
            # 比例和分辨率
            'aspect_ratio_index_wide = "21"',
            'video_vres = "29"',
            # 目录相关的设置
            'libretro_path = ""',
            f'libretro_directory = "{app_dir}"',
            f'screenshot_directory = "{data_dir}/screenshots"',
            f'system_directory = "{data_dir}/system"',
            f'extraction_directory = "{data_dir}/system/temp"',
            f'savefile_directory = "{data_dir}/savefiles"',
            f'savestate_directory = "{data_dir}/savestates"',
            f'video_filter_dir = "{data_dir}/videofilters"',
            f'audio_filter_dir = "{data_dir}/audiofilters"',
            f'rgui_browser_directory = "{self.configs.device}:/{rgui_browser_directory}"',
            f'overlay_directory = "{data_dir}/overlays"',
            f'input_overlay = "{data_dir}/overlays/..."',
            # 快捷键相关的设置
            'input_menu_combos = "1"',
            'input_load_state_axis = "-2"',
            'input_state_slot_decrease_axis = "-3"',
            'input_state_slot_increase_axis = "+3"',
            'input_menu_toggle_axis = "+2"',
            # 界面相关的设置
            'clock_posx = "240"',
            # 刷新率一律填 60
            'video_refresh_rate = "60.000000"',
        ]

        return list_ret

    def configs_dict(self):
        dict_ret = {}
        for line in self.configs_list():
            key = line[: line.find("=")]
            dict_ret[key] = line

        return dict_ret

    def export_main_cfg(self):
        dst_cfg_file_path = self.data_directory().joinpath("main.cfg")
        if dst_cfg_file_path.exists() and dst_cfg_file_path.is_file():
            dst_cfg_file_path.unlink()

        with open(dst_cfg_file_path, "w", encoding="utf-8") as dst_file:
            configs_dict = self.configs_dict()
            src_cfg_file_path = LocalConfigs.repository_directory().joinpath(
                f"wii\\apps\\{WiiRA_SS_Configs.core_folder_name()}",
                WiiRA_SS_Configs.core_cfg_template_file_name(),
            )
            with open(src_cfg_file_path, "r", encoding="utf-8") as src_file:
                line = src_file.readline()
                while line:
                    for key, value in configs_dict.items():
                        if line.startswith(key):
                            line = value + "\n"
                            break
                    dst_file.write(line)
                    line = src_file.readline()
            dst_file.close()

    def export_all(self):
        app_dir = self.app_directory()
        if not Helper.verify_exist_directory_ex(app_dir):
            print(f"【错误】无效的目标文件夹 {app_dir}")
            return

        data_dir = self.data_directory()
        if not Helper.verify_exist_directory_ex(data_dir):
            print(f"【错误】无效的目标文件夹 {data_dir}")
            return

        self.export_core_files()
        self.export_icon_png()
        self.export_meta_xml()
        self.export_main_cfg()
