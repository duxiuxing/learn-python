# -- coding: UTF-8 --

from game import Game
from games_db import GamesDB
from helper import Helper
from local_configs import LocalConfigs
from pathlib import Path
from PIL import Image
from resource_file_helper import ResourceFileHelper
from wii_ra_app_configs import WiiRA_AppConfigs
from wii_ra_configs import WiiRA_Configs
from wii_ra_ss_configs import WiiRA_SS_Configs
from wiiflow_configs import WiiFlow_Configs
from wiiflow_game import WiiFlow_Game
from wiiflow_games_db import WiiFlow_GamesDB
from wiiflow_rom import WiiFlow_Rom
from wiiflow_roms_db import WiiFlow_RomsDB


class WiiRA_App:
    def __init__(self, configs: WiiRA_AppConfigs):
        self.configs = configs

    def app_folder_name(self):
        return f"{self.configs.device}-{self.configs.folder_name}"

    def export_core_files(self):
        src_app_dir = LocalConfigs.repository_directory().joinpath(
            "wii\\apps", WiiRA_Configs.core_folder_name()
        )
        dst_app_dir = LocalConfigs.export_to_directory().joinpath(
            f"apps\\{self.app_folder_name()}"
        )

        src_dir = src_app_dir.joinpath("info")
        dst_dir = dst_app_dir.joinpath("info")
        Helper.copy_directory(src_dir, dst_dir)

        src_file_path = src_app_dir.joinpath(WiiRA_Configs.core_file_name())
        Helper.copy_file_to_directory(src_file_path, dst_app_dir)

        dst_file_path = dst_app_dir.joinpath("boot.dol")
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

        dst_icon_png_path = LocalConfigs.export_to_directory().joinpath(
            f"apps\\{self.app_folder_name()}\\icon.png"
        )
        if dst_icon_png_path.exists() and dst_icon_png_path.is_file():
            dst_icon_png_path.unlink()

        Image.open(src_icon_png_path).resize((128, 48)).save(dst_icon_png_path)

    def export_meta_xml(self):
        meta_xml_path = LocalConfigs.export_to_directory().joinpath(
            f"apps\\{self.app_folder_name()}\\meta.xml"
        )
        if meta_xml_path.exists() and meta_xml_path.is_file():
            meta_xml_path.unlink()

        with open(meta_xml_path, "w", encoding="utf-8") as xml_file:
            xml_file.write('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n')
            xml_file.write('<app version="1">\n')
            app_name = self.configs.app_name.replace("&", "&amp;")
            xml_file.write(f"  <name>{app_name}</name>\n")
            xml_file.write("  <author>Libretro &amp; R-Sam</author>\n")
            xml_file.write(
                f"  <version>{WiiRA_Configs.version()}.{self.configs.device}</version>\n"
            )
            xml_file.write(
                f"  <release_date>{WiiRA_Configs.release_date()}</release_date>\n"
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
            website = WiiFlow_Configs.website()
            if website is None:
                xml_file.write(
                    f"Wii Channel: {self.configs.device}:/wad/{lower_plugin_name}</long_description>\n"
                )
            else:
                xml_file.write(
                    f"Wii Channel: {self.configs.device}:/wad/{lower_plugin_name}\n"
                )
                xml_file.write(f"Website: {website}</long_description>\n")
            xml_file.write("  <no_ios_reload />\n")
            xml_file.write("  <ahb_access />\n")
            if len(self.configs.rom_file_path_list) == 1:
                rom_file_parent = str(
                    self.configs.rom_file_path_list[0].parent
                ).replace("\\", "/")
                xml_file.write("  <arguments>\n")
                xml_file.write(
                    f"    <arg>{self.configs.device}:/{rom_file_parent}</arg>\n"
                )
                xml_file.write(
                    f"    <arg>{self.configs.rom_file_path_list[0].name}</arg>\n"
                )
                xml_file.write("  </arguments>\n")

            xml_file.write("</app>\n")
            xml_file.close()

    def configs_list(self):
        app_dir = f"{self.configs.device}:/apps/{self.app_folder_name()}"
        retroarch_dir = f"{self.configs.device}:/retroarch"

        list_ret = [
            # 游戏画面宽高比：0=4:3 22=Core provided
            'aspect_ratio_index = "0"',
            # 分辨率：30=640x448
            'current_resolution_id = "30"',
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
            f'assets_directory = "{app_dir}/assets"',
            f'audio_filter_dir = "{app_dir}/filters/audio"',
            f'cheat_database_path = "{app_dir}/cheats"',
            f'content_favorites_path = "{app_dir}/playlists/builtin/content_favorites.lpl"',
            f'content_history_path = "{app_dir}/playlists/builtin/content_history.lpl"',
            f'content_image_history_path = "{app_dir}/playlists/builtin/content_image_history.lpl"',
            f'content_music_history_path = "{app_dir}/playlists/builtin/content_music_history.lpl"',
            f'content_video_history_path = "{app_dir}/playlists/builtin/content_video_history.lpl"',
            f'joypad_autoconfig_dir = "{app_dir}/autoconfig"',
            f'libretro_directory = "{app_dir}"',
            f'libretro_info_path = "{app_dir}/info"',
            f'log_dir = "{retroarch_dir}/logs"',
            f'osk_overlay_directory = "{app_dir}/overlays/keyboards"',
            f'savefile_directory = "{retroarch_dir}/savefiles"',
            f'savestate_directory = "{retroarch_dir}/savestates"',
            f'system_directory = "{retroarch_dir}/system"',
            f'video_filter_dir = "{app_dir}/filters/video"',
            # 刷新率一律填 60
            'crt_video_refresh_rate = "60.000000"',
            'video_refresh_rate = "60.000000"',
            # 提高性能
            'content_runtime_log = "false"',
            'savestate_file_compression = "false"',
        ]

        if len(self.configs.rom_file_path_list) > 10:
            list_ret.append('content_show_history = "true"')
            list_ret.append('content_show_playlists = "true"')
            list_ret.append('playlist_entry_remove_enable = "1"')
            list_ret.append('quick_menu_show_add_to_favorites = "true"')
            # 开始界面：5=Playlists
            list_ret.append('menu_startup_page = "5"')
        else:
            list_ret.append('content_show_history = "false"')
            list_ret.append('content_show_playlists = "false"')
            list_ret.append('playlist_entry_remove_enable = "2"')
            list_ret.append('quick_menu_show_add_to_favorites = "false"')
            # 开始界面：2=Favorites
            list_ret.append('menu_startup_page = "2"')

        if WiiRA_SS_Configs.data_folder_name() is None:
            list_ret.append(f'overlay_directory = "{app_dir}/overlays"')
        else:
            ra_ss_data_dir = (
                f"{self.configs.device}:/private/{WiiRA_SS_Configs.data_folder_name()}"
            )
            list_ret.append(f'overlay_directory = "{ra_ss_data_dir}/overlays"')

        return list_ret

    def configs_dict(self):
        dict_ret = {}
        for line in self.configs_list():
            key = line[: line.find("=")]
            dict_ret[key] = line

        return dict_ret

    def export_retroarch_cfg(self):
        dst_cfg_file_path = LocalConfigs.export_to_directory().joinpath(
            f"apps\\{self.app_folder_name()}\\{WiiRA_Configs.core_cfg_file_name()}"
        )

        if dst_cfg_file_path.exists() and dst_cfg_file_path.is_file():
            dst_cfg_file_path.unlink()

        with open(dst_cfg_file_path, "w", encoding="utf-8") as dst_file:
            configs_dict = self.configs_dict()
            src_cfg_file_path = LocalConfigs.repository_directory().joinpath(
                f"wii\\apps\\{WiiRA_Configs.core_folder_name()}",
                WiiRA_Configs.core_cfg_file_name(),
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

    def export_retroarch_salamander_cfg(self):
        cfg_file_path = LocalConfigs.export_to_directory().joinpath(
            f"apps\\{self.app_folder_name()}\\retroarch-salamander.cfg"
        )
        if cfg_file_path.exists() and cfg_file_path.is_file():
            cfg_file_path.unlink()

        with open(cfg_file_path, "w", encoding="utf-8") as cfg_file:
            core_path = f"{self.configs.device}:/apps/{self.configs.folder_name}-{self.configs.device}/{WiiRA_Configs.core_file_name()}"
            cfg_file.write(f'libretro_path = "{core_path}"\n')
            cfg_file.close()

    def export_lpl_file(self):
        lpl_file_path = LocalConfigs.export_to_directory().joinpath(
            f"apps\\{self.app_folder_name()}\\playlists\\builtin\\content_favorites.lpl"
        )
        if len(self.configs.rom_file_path_list) > 10:
            lpl_file_path = LocalConfigs.export_to_directory().joinpath(
                f"apps\\{self.app_folder_name()}\\playlists\\{WiiRA_Configs.db_name()}",
            )
        if not Helper.verify_exist_directory_ex(lpl_file_path.parent):
            print(f"【错误】无效的目标文件 {lpl_file_path}")
            return
        if lpl_file_path.exists() and lpl_file_path.is_file():
            lpl_file_path.unlink()

        with open(lpl_file_path, "w", encoding="utf-8") as lpl_file:
            core_path = f"{self.configs.device}:/apps/{self.configs.folder_name}-{self.configs.device}/{WiiRA_Configs.core_file_name()}"
            head = (
                "{\n"
                '  "version": "1.5",\n'
                f'  "default_core_path": "{core_path}",\n'
                f'  "default_core_name": "{WiiRA_Configs.core_name()}",\n'
                '  "label_display_mode": 0,\n'
                '  "right_thumbnail_mode": 3,\n'
                '  "left_thumbnail_mode": 2,\n'
                '  "thumbnail_match_mode": 0,\n'
                '  "sort_mode": 1,\n'
                '  "items": [\n'
            )
            lpl_file.write(head)

            first_rom = True
            for rom_file_path in self.configs.rom_file_path_list:
                if first_rom:
                    first_rom = False
                    lpl_file.write("    {\n")
                else:
                    lpl_file.write(",\n    {\n")

                rom_file_path = str(rom_file_path).replace("\\", "/")
                path = f"{self.configs.device}:/{rom_file_path}"
                lpl_file.write(f'      "path": "{path}",\n')

                rom_file_title = Path(rom_file_path).stem
                rom = WiiFlow_RomsDB.query_rom(rom_file_title=rom_file_title)
                game = GamesDB.query_game(game_id=rom.game_id)
                lpl_file.write(f'      "label": "{game.en_title}",\n')
                lpl_file.write(f'      "core_path": "{core_path}",\n')
                lpl_file.write(f'      "core_name": "{WiiRA_Configs.core_name()}",\n')
                lpl_file.write(f'      "crc32": "{rom.crc32}|crc",\n')
                lpl_file.write(f'      "db_name": "{WiiRA_Configs.db_name()}"\n')
                lpl_file.write("    }")

            lpl_file.write("\n  ]\n}\n")
            lpl_file.close()

    def export_all(self):
        app_dir = LocalConfigs.export_to_directory().joinpath(
            f"apps\\{self.app_folder_name()}"
        )
        if not Helper.verify_exist_directory_ex(app_dir):
            print(f"【错误】无效的目标文件夹 {app_dir}")
            return

        self.export_core_files()
        self.export_icon_png()
        self.export_meta_xml()
        self.export_retroarch_cfg()
        self.export_retroarch_salamander_cfg()
        self.export_lpl_file()
