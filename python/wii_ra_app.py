# -- coding: UTF-8 --

from game import Game
from games_db import GamesDB
from helper import Helper
from local_configs import LocalConfigs
from pathlib import Path
from PIL import Image
from ra_configs import RA_Configs
from ra_playlist import RA_Playlist
from resource_file_helper import ResourceFileHelper
from wii_app_configs import Wii_AppConfigs
from wii_ra_configs import WiiRA_Configs
from wiiflow_configs import WiiFlow_Configs
from wiiflow_game import WiiFlow_Game
from wiiflow_games_db import WiiFlow_GamesDB
from wiiflow_rom import WiiFlow_Rom
from wiiflow_roms_db import WiiFlow_RomsDB


class WiiRA_App:
    def __init__(self, app_configs: Wii_AppConfigs):
        self.configs = app_configs

    def app_folder_name(self):
        plugin_name = WiiFlow_Configs.plugin_name.lower()
        if plugin_name == self.configs.app_folder_base_name:
            return f"{self.configs.device}-{plugin_name}"
        else:
            return f"{self.configs.device}-{plugin_name}-{self.configs.app_folder_base_name}"

    def win_app_directory(self) -> Path:
        return LocalConfigs.export_to_directory.joinpath(
            f"apps\\{self.app_folder_name()}"
        )

    def wii_app_directory(self) -> str:
        return f"{self.configs.device}:/apps/{self.app_folder_name()}"

    # 拷贝 boot.dol，如果是模拟器 App 还要拷贝 core 和 info 文件
    def export_core_files(self):
        src_dir = WiiRA_Configs.repository_directory()
        src_core_file_path = src_dir.joinpath(WiiRA_Configs.core_file_name)

        if self.configs.playlist_configs is not None:
            src_core_info_file_path = src_dir.joinpath(
                f"info\\{WiiRA_Configs.core_info_file_name}"
            )
            dst_info_dir = self.win_app_directory().joinpath("info")
            Helper.copy_file_to_directory(src_core_info_file_path, dst_info_dir)
            Helper.copy_file_to_directory(src_core_file_path, self.win_app_directory())

        Helper.copy_file_if_not_exist(
            src_core_file_path, self.win_app_directory().joinpath("boot.dol")
        )

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

        dst_icon_png_path = self.win_app_directory().joinpath("icon.png")
        if dst_icon_png_path.exists() and dst_icon_png_path.is_file():
            dst_icon_png_path.unlink()

        Image.open(src_icon_png_path).resize((128, 48)).save(dst_icon_png_path)

    def export_meta_xml(self):
        meta_xml_path = self.win_app_directory().joinpath("meta.xml")
        if meta_xml_path.exists() and meta_xml_path.is_file():
            meta_xml_path.unlink()

        with open(meta_xml_path, "w", encoding="utf-8") as xml_file:
            xml_file.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n')
            xml_file.write('<app version="1">\n')
            app_name = self.configs.app_name.replace("&", "&amp;")
            xml_file.write(f"  <name>{app_name}</name>\n")
            xml_file.write("  <author>Libretro &amp; R-Sam</author>\n")
            xml_file.write(
                f"  <version>{WiiRA_Configs.version}.{self.configs.device}</version>\n"
            )
            xml_file.write(
                f"  <release_date>{WiiRA_Configs.release_date}</release_date>\n"
            )
            xml_file.write(
                f"  <short_description>{self.configs.short_description()}</short_description>\n"
            )
            xml_file.write(f"  <long_description>{self.configs.long_description}")

            lower_plugin_name = WiiFlow_Configs.plugin_name.lower()
            website = WiiFlow_Configs.website
            if website is None:
                xml_file.write("</long_description>\n")
            else:
                xml_file.write(f"\n\nWebsite: {website}</long_description>\n")
            xml_file.write("  <ahb_access/>\n")

            if self.configs.rom is not None:
                xml_file.write("  <arguments>\n")
                xml_file.write(
                    f"    <arg>{WiiRA_Configs.wii_roms_directory(self.configs.device)}</arg>\n"
                )
                rom_file_name = self.configs.rom.file_name().replace("&", "&amp;")
                xml_file.write(f"    <arg>{rom_file_name}</arg>\n")
                xml_file.write("  </arguments>\n")

            xml_file.write("</app>\n")
            xml_file.close()

    def settings_list(self):
        app_dir = self.wii_app_directory()
        retroarch_dir = WiiRA_Configs.wii_data_directory(self.configs.device)

        list_ret = [
            # 游戏画面宽高比：0=4:3 1=16:9 22=Core provided
            'aspect_ratio_index = "0"',
            # 分辨率：0=默认 24=384x448 30=640x448
            # 各个机种的分辨率不一定相同，可通过 WiiRA_Configs.settings_list 指定
            'current_resolution_id = "0"',
            # 菜单界面宽高比：11=Auto
            'rgui_aspect_ratio = "11"',
            # 配色：29=Tango Dark
            'rgui_menu_color_theme = "29"',
            # 目录相关的设置
            f'playlist_directory = "{app_dir}/playlists"',
            f'rgui_config_directory = "{retroarch_dir}/config"',
            f'thumbnails_directory = "{retroarch_dir}/thumbnails"',
            # 在游戏列表中显示缩略图
            'menu_thumbnails = "2"',
            'menu_left_thumbnails = "1"',
            'rgui_inline_thumbnails = "true"',
            # 在游戏过程中使用手柄的左摇杆
            'input_max_users = "4"',
            'input_player1_analog_dpad_mode = "3"',
            'input_player2_analog_dpad_mode = "3"',
            'input_player3_analog_dpad_mode = "3"',
            'input_player4_analog_dpad_mode = "3"',
            # 菜单快捷键：右摇杆的下
            'input_menu_toggle_axis = "+3"',
            # 菜单快捷组合键：十字键的下+Z
            'input_menu_toggle_gamepad_combo = "9"',
            # 加载进度快捷键：右摇杆的上
            'input_load_state_axis = "-3"',
            # 上一个存档槽位：右摇杆的左
            'input_state_slot_decrease_axis = "-2"',
            # 下一个存档槽位：右摇杆的右
            'input_state_slot_increase_axis = "+2"',
            'menu_swap_ok_cancel_buttons = "false"',
            # 精简 MAIN MENU 界面
            'content_show_netplay = "false"',
            'menu_show_load_content = "false"',
            'menu_show_load_core = "false"',
            'menu_show_configurations = "false"',
            'menu_show_information = "false"',
            # 精简 PLAYLISTS 界面
            'content_show_add_entry = "0"',
            'content_show_explore = "false"',
            'playlist_entry_rename = "false"',
            # 精简游戏的快捷菜单界面
            'menu_show_latency = "false"',
            'menu_show_overlays = "false"',
            'menu_show_rewind = "false"',
            'quick_menu_show_cheats = "false"',
            'quick_menu_show_download_thumbnails = "false"',
            'quick_menu_show_options = "false"',
            'quick_menu_show_save_content_dir_overrides = "false"',
            'quick_menu_show_save_core_overrides = "false"',
            'quick_menu_show_save_game_overrides = "false"',
            'quick_menu_show_set_core_association = "false"',
            'quick_menu_show_reset_core_association = "false"',
            'quick_menu_show_start_recording = "false"',
            'quick_menu_show_start_streaming = "false"',
            'quick_menu_show_undo_save_load_state = "false"',
            # 其他
            f'assets_directory = "{retroarch_dir}/assets"',
            f'audio_filter_dir = "{retroarch_dir}/filters/audio"',
            f'cheat_database_path = "{retroarch_dir}/cheats"',
            f'content_favorites_path = "{app_dir}/playlists/builtin/content_favorites.lpl"',
            f'content_history_path = "{app_dir}/playlists/builtin/content_history.lpl"',
            f'content_image_history_path = "{app_dir}/playlists/builtin/content_image_history.lpl"',
            f'content_music_history_path = "{app_dir}/playlists/builtin/content_music_history.lpl"',
            f'content_video_history_path = "{app_dir}/playlists/builtin/content_video_history.lpl"',
            f'joypad_autoconfig_dir = "{retroarch_dir}/autoconfig"',
            f'libretro_directory = "{app_dir}"',
            f'libretro_info_path = "{app_dir}/info"',
            f'log_dir = "{retroarch_dir}/logs"',
            f'osk_overlay_directory = "{retroarch_dir}/overlays/keyboards"',
            f'overlay_directory = "{retroarch_dir}/overlays"',
            f'savefile_directory = "{retroarch_dir}/savefiles"',
            f'savestate_directory = "{retroarch_dir}/savestates"',
            f'system_directory = "{retroarch_dir}/system"',
            f'video_filter_dir = "{retroarch_dir}/filters/video"',
            # 刷新率一律填 60
            'crt_video_refresh_rate = "60.000000"',
            'video_refresh_rate = "60.000000"',
            # 提高性能
            'content_runtime_log = "false"',
            'savestate_file_compression = "false"',
        ]

        if self.configs.rom is not None:
            list_ret.append('content_show_favorites = "false"')
            list_ret.append('content_show_history = "false"')
            list_ret.append('content_show_playlists = "false"')
            list_ret.append('menu_show_restart_retroarch = "false"')
            list_ret.append('playlist_entry_remove_enable = "2"')
            list_ret.append('quick_menu_show_add_to_favorites = "false"')
            list_ret.append('quit_on_close_content = "2"')
        elif self.configs.use_favorites_as_playlist:
            list_ret.append('content_show_favorites = "true"')
            list_ret.append('content_show_history = "false"')
            list_ret.append('content_show_playlists = "false"')
            list_ret.append('menu_show_restart_retroarch = "true"')
            list_ret.append('playlist_entry_remove_enable = "2"')
            list_ret.append('quick_menu_show_add_to_favorites = "false"')
            list_ret.append('quit_on_close_content = "0"')
        else:
            list_ret.append('content_show_favorites = "true"')
            list_ret.append('content_show_history = "true"')
            list_ret.append('content_show_playlists = "true"')
            list_ret.append('menu_show_restart_retroarch = "true"')
            list_ret.append('playlist_entry_remove_enable = "1"')
            list_ret.append('quick_menu_show_add_to_favorites = "true"')
            list_ret.append('quit_on_close_content = "0"')

        if WiiRA_Configs.settings_list is not None:
            for line in WiiRA_Configs.settings_list:
                list_ret.append(line)

        return list_ret

    def configs_dict(self):
        dict_ret = {}
        for line in self.settings_list():
            key = line[: line.find("=")]
            dict_ret[key] = line

        return dict_ret

    def cfg_file_path(self) -> Path:
        if self.configs.cfg_file_name is None:
            return self.win_app_directory().joinpath(
                WiiRA_Configs.default_cfg_file_name
            )
        else:
            return LocalConfigs.export_to_directory.joinpath(
                f"retroarch\\{self.configs.cfg_file_name}"
            )

    def export_retroarch_cfg(self):
        dst_cfg_file_path = self.cfg_file_path()
        if dst_cfg_file_path.exists() and dst_cfg_file_path.is_file():
            dst_cfg_file_path.unlink()

        with open(dst_cfg_file_path, "w", encoding="utf-8") as dst_file:
            configs_dict = self.configs_dict()
            src_cfg_file_path = WiiRA_Configs.repository_directory().joinpath(
                WiiRA_Configs.default_cfg_file_name,
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

    def core_file_wii_path(self):
        return f"{self.wii_app_directory()}/{WiiRA_Configs.core_file_name}"

    def export_playlist(self):
        if self.configs.playlist_configs is None:
            return

        lpl_file_path = self.win_app_directory().joinpath(
            f"playlists\\{RA_Configs.lpl_file_name}",
        )
        if self.configs.use_favorites_as_playlist:
            lpl_file_path = self.win_app_directory().joinpath(
                f"playlists\\builtin\\content_favorites.lpl"
            )

        if not Helper.verify_exist_directory_ex(lpl_file_path.parent):
            print(f"【错误】无效的目标文件 {lpl_file_path}")
            return
        if lpl_file_path.exists() and lpl_file_path.is_file():
            lpl_file_path.unlink()

        self.configs.playlist_configs.lpl_file_path = lpl_file_path
        self.configs.playlist_configs.set_head(
            "{\n"
            '  "version": "1.5",\n'
            f'  "default_core_path": "{self.core_file_wii_path()}",\n'
            f'  "default_core_name": "{WiiRA_Configs.core_name}",\n'
            '  "label_display_mode": 0,\n'
            '  "right_thumbnail_mode": 3,\n'
            '  "left_thumbnail_mode": 2,\n'
            '  "thumbnail_match_mode": 0,\n'
            '  "sort_mode": 1,\n'
            '  "items": [\n'
        )
        self.configs.playlist_configs.png_file_match_rom_file = True
        playlist = RA_Playlist(self.configs.playlist_configs)
        playlist.export_lpl_file()
        old_dir = LocalConfigs.export_to_directory
        LocalConfigs.export_to_directory = LocalConfigs.export_to_directory.joinpath(
            "retroarch"
        )
        playlist.export_thumbnails_boxarts()
        playlist.export_thumbnails_logos()
        playlist.export_thumbnails_snaps()
        playlist.export_thumbnails_titles()
        LocalConfigs.export_to_directory = old_dir

    def export_remap_file(self):
        if self.configs.rom is None or self.configs.remap is None:
            return

        src_file_path = WiiRA_Configs.repository_directory().joinpath(
            f"remaps\\{self.configs.remap}.rmp"
        )
        dst_file_path = LocalConfigs.export_to_directory.joinpath(
            f"{WiiRA_Configs.remaps_relative_directory}\\{self.configs.rom.file_title}.rmp"
        )
        if dst_file_path.exists() and dst_file_path.is_file():
            dst_file_path.unlink()
        Helper.copy_file_if_not_exist(src_file_path, dst_file_path)

    def export_all(self):
        app_dir = self.win_app_directory()
        if not Helper.verify_exist_directory_ex(app_dir):
            print(f"【错误】无效的目标文件夹 {app_dir}")
            return

        self.export_core_files()
        self.export_icon_png()
        self.export_meta_xml()
        self.export_retroarch_cfg()
        self.export_playlist()
        self.export_remap_file()
