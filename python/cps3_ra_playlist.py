# -- coding: UTF-8 --

from game import Game
from games_db import GamesDB
from init_global_configs import Init_Global_Configs
from local_configs import LocalConfigs
from pathlib import Path
from ra_configs import RA_Configs
from ra_playlist import RA_Playlist
from ra_playlist_config import RA_PlaylistConfig
from ra_playlist_item import RA_PlaylistItem
from rom import Rom
from roms_db import RomsDB

cps3_rom_file_name_list = [
    # C - 赤色大地
    "redearth.zip",
    # J - JOJO的奇妙冒险1
    "jojon.zip",
    # J - JOJO的奇妙冒险2 未来遗产
    "jojobaner1.zip",
    # J - 街头霸王3.1 新纪元
    "sfiiin.zip",
    # J - 街头霸王3.2 巨型打击
    "sfiii2.zip",
    # J - 街头霸王3.3 未来战斗
    "sfiii3.zip",
]

if __name__ == "__main__":
    Init_Global_Configs()

    configs = RA_PlaylistConfig()

    while True:
        export_to_dir = LocalConfigs.export_to_directory
        print(
            f"\n即将导出列表和缩略图到目标文件夹\n默认目标文件夹路径：{export_to_dir}"
        )
        user_input = input("请确认目标文件夹路径，使用默认路径请直接按回车 > ")
        if len(user_input) > 0:
            export_to_dir = Path(user_input)

        if export_to_dir.exists() and export_to_dir.is_dir():
            LocalConfigs.export_to_directory = export_to_dir
        else:
            print(f"【错误】无效的文件夹路径：{export_to_dir}")
            continue

        print(
            "\n1. Android\n"
            "2. iPad\n"
            "3. PS3\n"
            "4. Windows\n"
            "5. XBOX\n"
            "其他输入表示退出"
        )
        user_input = input("请选择 RetroArch 的版本，输入对应的序号 > ")
        try:
            number = int(user_input)
            if number == 1:
                # Android
                for rom_file_name in cps3_rom_file_name_list:
                    rom = RomsDB.query_rom(rom_file_name=rom_file_name)
                    game = GamesDB.query_game(game_id=rom.game_id)
                    item = RA_PlaylistItem(
                        path=f"/storage/emulated/0/arcade/cps3/{rom_file_name}",
                        label=game.zhcn_title,
                        crc32=rom.crc32,
                        db_name=RA_Configs.lpl_file_name(),
                    )
                    configs.item_list.append(item)

                configs.png_file_match_rom_file = True
                configs.boxarts_folder = "boxart-stuartc49"
                configs.logos_folder = "logo"
                configs.snaps_folder = "snap"
                configs.titles_folder = "title"
                break
            elif number == 2:
                # iPad
                for rom_file_name in cps3_rom_file_name_list:
                    rom = RomsDB.query_rom(rom_file_name=rom_file_name)
                    game = GamesDB.query_game(game_id=rom.game_id)
                    item = RA_PlaylistItem(
                        path=f"~/Documents/RetroArch/arcade/cps3/{rom_file_name}",
                        label=game.zhcn_title,
                        crc32=rom.crc32,
                        db_name=RA_Configs.lpl_file_name(),
                    )
                    configs.item_list.append(item)

                configs.png_file_match_rom_file = True
                configs.boxarts_folder = "boxart-stuartc49"
                configs.logos_folder = "logo"
                configs.snaps_folder = "snap"
                configs.titles_folder = "title"
                break
            elif number == 3:
                # PS3
                for rom_file_name in cps3_rom_file_name_list:
                    rom = RomsDB.query_rom(rom_file_name=rom_file_name)
                    game = GamesDB.query_game(game_id=rom.game_id)
                    item = RA_PlaylistItem(
                        path=f"/dev_hdd0/game/RETROARCH/USRDIR/arcade/cps3/{rom_file_name}",
                        label=game.zhcn_title,
                        crc32=rom.crc32,
                        db_name=RA_Configs.lpl_file_name(),
                    )
                    configs.item_list.append(item)

                configs.png_file_match_rom_file = False
                configs.boxarts_folder = "boxart-stuartc49"
                configs.logos_folder = None
                configs.snaps_folder = "snap"
                configs.titles_folder = "title"
                break
            elif number == 4:
                # Windows
                for rom_file_name in cps3_rom_file_name_list:
                    rom = RomsDB.query_rom(rom_file_name=rom_file_name)
                    game = GamesDB.query_game(game_id=rom.game_id)
                    item = RA_PlaylistItem(
                        path=f"X:\\\\arcade\\\\cps3\\\\{rom_file_name}",
                        label=game.zhcn_title,
                        crc32=rom.crc32,
                        db_name=RA_Configs.lpl_file_name(),
                    )
                    configs.item_list.append(item)

                configs.png_file_match_rom_file = True
                configs.boxarts_folder = "boxart-stuartc49"
                configs.logos_folder = "logo"
                configs.snaps_folder = "snap"
                configs.titles_folder = "title"
                break
            elif number == 5:
                # XBOX
                for rom_file_name in cps3_rom_file_name_list:
                    rom = RomsDB.query_rom(rom_file_name=rom_file_name)
                    game = GamesDB.query_game(game_id=rom.game_id)
                    item = RA_PlaylistItem(
                        path=f"E:\\\\arcade\\\\cps3\\\\{rom_file_name}",
                        label=game.zhcn_title,
                        crc32=rom.crc32,
                        db_name=RA_Configs.lpl_file_name(),
                    )
                    configs.item_list.append(item)

                configs.png_file_match_rom_file = True
                configs.boxarts_folder = "boxart-stuartc49"
                configs.logos_folder = "logo"
                configs.snaps_folder = "snap"
                configs.titles_folder = "title"
                break
            else:
                exit()
        except ValueError:
            exit()

    while True:
        print(
            "\n1. 导出 ROM 文件\n"
            "2. 导出列表文件\n"
            "3. 导出 Boxarts 文件\n"
            "4. 导出 Logos 文件\n"
            "5. 导出 Snaps 文件\n"
            "6. 导出 Titles 文件\n"
            "7. 导出所有文件\n"
            "其他输入表示退出"
        )
        user_input = input("请输入操作的序号 > ")
        try:
            number = int(user_input)
            if number == 1:
                RA_Playlist(configs).export_rom_files()
            elif number == 2:
                RA_Playlist(configs).export_lpl_file()
            elif number == 3:
                RA_Playlist(configs).export_thumbnails_boxarts()
            elif number == 4:
                RA_Playlist(configs).export_thumbnails_logos()
            elif number == 5:
                RA_Playlist(configs).export_thumbnails_snaps()
            elif number == 6:
                RA_Playlist(configs).export_thumbnails_titles()
            elif number == 7:
                RA_Playlist(configs).export_all()
            else:
                exit()
        except ValueError:
            exit()
