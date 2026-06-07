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

cps1_rom_file_name_list = [
    # # - 1941 反击战
    "1941.zip",
    # C - 出击飞龙
    "strider.zip",
    # C - 惩罚者
    "punisher.zip",
    # C - 雌虎战机
    "cawing.zip",
    # D - 大魔界村
    "ghouls.zip",
    # J - 街头霸王2 四大天王
    "sf2ce.zip",
    # J - 街头霸王2 天下斗士
    "sf2.zip",
    # J - 街头霸王2 战斗宣言
    "sf2hf.zip",
    # K - 快打旋风
    "ffight.zip",
    # K - 恐龙快打
    "dino.zip",
    # L - 洛克人1 力量之战 (CPS1版)
    "megaman.zip",
    # L - 龙之迷题
    "qad.zip",
    # L - 龙王战士
    "kod.zip",
    # M - 冒险问答 卡普空世界2
    "cworld2j.zip",
    # M - 名将
    "captcomm.zip",
    # M - 梦幻冒险
    "nemo.zip",
    # M - 魔法剑 英雄的幻想
    "msword.zip",
    # M - 魔法方块
    "pnickj.zip",
    # M - 魔鬼气泡3
    "pang3.zip",
    # Q - 奇迹三世界
    "3wonders.zip",
    # S - 双麒儿
    "mtwins.zip",
    # S - 失落的世界
    "forgottnu.zip",
    # S - 少年街霸1 (CPS1版)
    "sfzch.zip",
    # S - 摔角霸王1
    "slammast.zip",
    # S - 摔角霸王1 最终之战
    "mbombrd.zip",
    # T - 吞食天地1 王朝战争
    "dynwar.zip",
    # T - 吞食天地2 赤壁之战
    "wof.zip",
    # W - 威洛之旅
    "willowj.zip",
    # W - 威虎战机 雷暴行动
    "varth.zip",
    # W - 问答 信长之野望2
    "qtono2j.zip",
    # Y - 圆桌骑士
    "knights.zip",
    # Z - 战区88
    "unsquad.zip",
    # Z - 战场之狼2
    "mercs.zip",
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
                for rom_file_name in cps1_rom_file_name_list:
                    rom = RomsDB.query_rom(rom_file_name=rom_file_name)
                    game = GamesDB.query_game(game_id=rom.game_id)
                    item = RA_PlaylistItem(
                        path=f"/storage/emulated/0/arcade/cps1/{rom_file_name}",
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
                for rom_file_name in cps1_rom_file_name_list:
                    rom = RomsDB.query_rom(rom_file_name=rom_file_name)
                    game = GamesDB.query_game(game_id=rom.game_id)
                    item = RA_PlaylistItem(
                        path=f"~/Documents/RetroArch/arcade/cps1/{rom_file_name}",
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
                for rom_file_name in cps1_rom_file_name_list:
                    rom = RomsDB.query_rom(rom_file_name=rom_file_name)
                    game = GamesDB.query_game(game_id=rom.game_id)
                    item = RA_PlaylistItem(
                        path=f"/dev_hdd0/game/RETROARCH/USRDIR/arcade/cps1/{rom_file_name}",
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
                for rom_file_name in cps1_rom_file_name_list:
                    rom = RomsDB.query_rom(rom_file_name=rom_file_name)
                    game = GamesDB.query_game(game_id=rom.game_id)
                    item = RA_PlaylistItem(
                        path=f"X:\\\\arcade\\\\cps1\\\\{rom_file_name}",
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
                for rom_file_name in cps1_rom_file_name_list:
                    rom = RomsDB.query_rom(rom_file_name=rom_file_name)
                    game = GamesDB.query_game(game_id=rom.game_id)
                    item = RA_PlaylistItem(
                        path=f"E:\\\\arcade\\\\cps1\\\\{rom_file_name}",
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
