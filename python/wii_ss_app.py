# -- coding: UTF-8 --

from game import Game
from games_db import GamesDB
from helper import Helper
from local_configs import LocalConfigs
from pathlib import Path
from PIL import Image
from resource_file_helper import ResourceFileHelper
from wii_app_configs import Wii_AppConfigs
from wii_ra_configs import WiiRA_Configs
from wii_ss_configs import WiiSS_Configs
from wiiflow_configs import WiiFlow_Configs
from wiiflow_game import WiiFlow_Game
from wiiflow_games_db import WiiFlow_GamesDB
from wiiflow_rom import WiiFlow_Rom
from wiiflow_roms_db import WiiFlow_RomsDB


class WiiSS_App:
    def __init__(self, configs: Wii_AppConfigs):
        self.configs = configs

    def app_folder_name(self):
        return f"{self.configs.device}-{self.configs.base_app_folder_name}-ss"

    def app_folder_win_path(self) -> Path:
        return LocalConfigs.export_to_directory.joinpath(
            f"apps\\{self.app_folder_name()}"
        )

    def app_folder_wii_path(self) -> str:
        return f"{self.configs.device}:/apps/{self.app_folder_name()}"

    def boot_dol_win_path(self) -> Path:
        return self.app_folder_win_path().joinpath("boot.dol")

    def icon_png_win_path(self) -> Path:
        return self.app_folder_win_path().joinpath("icon.png")

    def meta_xml_win_path(self) -> Path:
        return self.app_folder_win_path().joinpath("meta.xml")

    def data_folder_win_path(self) -> Path:
        return LocalConfigs.export_to_directory.joinpath(
            f"private\\{WiiSS_Configs.data_folder_name}"
        )

    def data_folder_wii_path(self) -> str:
        return f"{self.configs.device}:/private/{WiiSS_Configs.data_folder_name}"

    # 拷贝 boot.dol
    def export_core_files(self):
        src_core_file_path = WiiSS_Configs.src_app_directory().joinpath(
            WiiSS_Configs.core_file_name,
        )
        Helper.copy_file_if_not_exist(src_core_file_path, self.boot_dol_win_path())

    # logo 转 icon
    def export_icon_png(self):
        game = Game(id=None, en_title=self.configs.app_name, zhcn_title=None)
        src_icon_png_path = ResourceFileHelper.compute_game_media_file_path(
            game, "logo", ".png"
        )
        if not src_icon_png_path.exists():
            game = GamesDB.query_game(game_id=self.configs.rom.game_id)
            src_icon_png_path = ResourceFileHelper.compute_game_media_file_path(
                game, "logo", ".png"
            )
            if not src_icon_png_path.exists():
                print(f"【错误】无效的源文件 {src_icon_png_path}")
                return

        dst_icon_png_path = self.icon_png_win_path()
        if dst_icon_png_path.exists() and dst_icon_png_path.is_file():
            dst_icon_png_path.unlink()

        Image.open(src_icon_png_path).resize((128, 48)).save(dst_icon_png_path)

    def export_meta_xml(self):
        meta_xml_path = self.meta_xml_win_path()
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
                f"  <release_date>{WiiSS_Configs.release_date}</release_date>\n"
            )
            xml_file.write(
                f"  <short_description>{self.configs.short_description()}</short_description>\n"
            )
            xml_file.write(f"  <long_description>{self.configs.long_description}\n\n")

            lower_plugin_name = WiiFlow_Configs.plugin_name.lower()
            website = WiiFlow_Configs.website
            if website is None:
                xml_file.write(
                    f"Wii Channel: {self.configs.device}:/wad/{lower_plugin_name}</long_description>\n"
                )
            else:
                xml_file.write(
                    f"Wii Channel: {self.configs.device}:/wad/{lower_plugin_name}\n"
                )
                xml_file.write(f"Website: {website}</long_description>\n")
            xml_file.write("  <ahb_access/>\n")

            if self.configs.rom is not None:
                xml_file.write("  <arguments>\n")
                xml_file.write(
                    f"    <arg>{WiiRA_Configs.rom_folder_wii_path(self.configs.device)}</arg>\n"
                )
                rom_file_name = self.configs.rom.file_name().replace("&", "&amp;")
                xml_file.write(f"    <arg>{rom_file_name}</arg>\n")
                xml_file.write(
                    f"    <arg>{self.data_folder_wii_path()}/{self.configs.rom.file_title}.cfg</arg>\n"
                )
                xml_file.write("  </arguments>\n")

            xml_file.write("</app>\n")
            xml_file.close()

    def settings_list(self):
        data_dir = self.data_folder_wii_path()

        list_ret = [
            # 宽高比：0=4:3 1=16:9 21=Core provided
            'aspect_ratio_index = "0"',
            'aspect_ratio_index_wide = "0"',
            # 分辨率：21=640x448 29=640x480 31=640x456
            'video_vres = "31"',
            # 目录相关的设置
            'libretro_path = "."',
            'libretro_directory = "."',
            f'screenshot_directory = "{data_dir}/screenshots"',
            'video_filter = "."',
            'audio_dsp_plugin = "."',
            f'system_directory = "{data_dir}/system"',
            f'extraction_directory = "{data_dir}/system/temp"',
            f'savefile_directory = "{data_dir}/savefiles"',
            f'savestate_directory = "{data_dir}/savestates"',
            f'video_filter_dir = "{data_dir}/videofilters"',
            f'audio_filter_dir = "{data_dir}/audiofilters"',
            f'rgui_browser_directory = "{WiiRA_Configs.rom_folder_wii_path(self.configs.device)}"',
            f'overlay_directory = "{data_dir}/overlays"',
            f'input_overlay = "{data_dir}/overlays/..."',
            # 菜单快捷组合键：L+R+Z+Start
            'input_menu_combos = "1"',
            # 加载进度快捷键：右摇杆的上
            'input_load_state_axis = "-3"',
            # 上一个存档槽位：右摇杆的左
            'input_state_slot_decrease_axis = "-2"',
            # 下一个存档槽位：右摇杆的右
            'input_state_slot_increase_axis = "+2"',
            # 菜单快捷键：右摇杆的下
            'input_menu_toggle_axis = "+3"',
            # 界面相关的设置
            'menu_solid = "true"',
            'menu_fullscreen = "true"',
            'hide_core = "true"',
            'hide_curr_state = "false"',
            'clock_posx = "240"',
            # 刷新率一律填 60
            'video_refresh_rate = "60.000000"',
        ]

        return list_ret

    def configs_dict(self):
        dict_ret = {}
        for line in self.settings_list():
            key = line[: line.find("=")]
            dict_ret[key] = line

        return dict_ret

    def export_cfg_file(self):
        dst_cfg_file_path = self.data_directory().joinpath("main.cfg")
        if len(self.configs.rom_file_relative_path_list) == 1:
            dst_cfg_file_path = self.data_directory().joinpath(
                f"{self.configs.rom_file_relative_path_list[0].stem}.cfg"
            )
        if dst_cfg_file_path.exists() and dst_cfg_file_path.is_file():
            dst_cfg_file_path.unlink()

        with open(dst_cfg_file_path, "w", encoding="utf-8") as dst_file:
            configs_dict = self.configs_dict()
            src_cfg_file_path = WiiSS_Configs.src_app_directory().joinpath(
                WiiSS_Configs.core_cfg_template_file_name(),
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
        app_dir = LocalConfigs.export_to_directory.joinpath(
            f"apps\\{self.app_folder_name()}"
        )
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
        self.export_cfg_file()
