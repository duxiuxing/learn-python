# -- coding: UTF-8 --

from game import Game
from games_db import GamesDB
from init_global_configs import Init_Global_Configs
from local_configs import LocalConfigs
from pathlib import Path
from ra_configs import RA_Configs
from ra_playlist import RA_Playlist
from ra_playlist_configs import RA_PlaylistConfigs
from ra_playlist_item import RA_PlaylistItem
from rom import Rom
from roms_db import RomsDB

cps1_lite_rom_list = [
    # # - 1941 反击战
    Rom("1941.zip"),
    # C - 出击飞龙
    Rom("strider.zip"),
    # C - 惩罚者
    Rom("punisher.zip"),
    # C - 雌虎战机
    Rom("cawing.zip"),
    # D - 大魔界村
    Rom("ghouls.zip"),
    # J - 街头霸王2 四大天王
    Rom("sf2ce.zip"),
    # J - 街头霸王2 天下斗士
    Rom("sf2.zip"),
    # J - 街头霸王2 战斗宣言
    Rom("sf2hf.zip"),
    # K - 快打旋风
    Rom("ffight.zip"),
    # K - 恐龙快打
    Rom("dino.zip"),
    # L - 洛克人1 力量之战 (CPS1版)
    Rom("megaman.zip"),
    # L - 龙之迷题
    Rom("qad.zip"),
    # L - 龙王战士
    Rom("kod.zip"),
    # M - 冒险问答 卡普空世界2
    Rom("cworld2j.zip"),
    # M - 名将
    Rom("captcomm.zip"),
    # M - 梦幻冒险
    Rom("nemo.zip"),
    # M - 魔法剑 英雄的幻想
    Rom("msword.zip"),
    # M - 魔法方块
    Rom("pnickj.zip"),
    # M - 魔鬼气泡3
    Rom("pang3.zip"),
    # Q - 奇迹三世界
    Rom("3wonders.zip"),
    # S - 双麒儿
    Rom("mtwins.zip"),
    # S - 失落的世界
    Rom("forgottn.zip"),
    # S - 少年街霸 (CPS1版)
    Rom("sfzch.zip"),
    # S - 摔角霸王1
    Rom("slammast.zip"),
    # S - 摔角霸王1 最终之战
    Rom("mbombrd.zip"),
    # T - 吞食天地1 王朝战争
    Rom("dynwar.zip"),
    # T - 吞食天地2 赤壁之战
    Rom("wof.zip"),
    # W - 威洛之旅
    Rom("willowj.zip"),
    # W - 威虎战机 雷暴行动
    Rom("varth.zip"),
    # W - 问答 信长之野望2
    Rom("qtono2j.zip"),
    # Y - 圆桌骑士
    Rom("knights.zip"),
    # Z - 战区88
    Rom("unsquad.zip"),
    # Z - 战场之狼2
    Rom("mercs.zip"),
]

if __name__ == "__main__":
    Init_Global_Configs()

    configs = RA_PlaylistConfigs()
    configs.roms_relative_directory = RA_Configs.win_roms_relative_directory

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
                for lite_rom in cps1_lite_rom_list:
                    rom = RomsDB.query_rom(
                        rom_crc32=lite_rom.crc32, rom_file_name=lite_rom.file_name
                    )
                    game = GamesDB.query_game(game_id=rom.game_id)
                    item = RA_PlaylistItem(
                        path=f"{RA_Configs.android_roms_directory}/{rom.file_name}",
                        label=game.zhcn_title,
                        crc32=rom.crc32,
                        db_name=RA_Configs.lpl_file_name,
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
                for lite_rom in cps1_lite_rom_list:
                    rom = RomsDB.query_rom(
                        rom_crc32=lite_rom.crc32, rom_file_name=lite_rom.file_name
                    )
                    game = GamesDB.query_game(game_id=rom.game_id)
                    item = RA_PlaylistItem(
                        path=f"{RA_Configs.ipad_roms_directory}/{rom.file_name}",
                        label=game.zhcn_title,
                        crc32=rom.crc32,
                        db_name=RA_Configs.lpl_file_name,
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
                for lite_rom in cps1_lite_rom_list:
                    rom = RomsDB.query_rom(
                        rom_crc32=lite_rom.crc32, rom_file_name=lite_rom.file_name
                    )
                    game = GamesDB.query_game(game_id=rom.game_id)
                    item = RA_PlaylistItem(
                        path=f"{RA_Configs.ps3_roms_directory}/{rom.file_name}",
                        label=game.zhcn_title,
                        crc32=rom.crc32,
                        db_name=RA_Configs.lpl_file_name,
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
                path_prefix = str(RA_Configs.win_roms_directory).replace("\\", "\\\\")
                for lite_rom in cps1_lite_rom_list:
                    rom = RomsDB.query_rom(
                        rom_crc32=lite_rom.crc32, rom_file_name=lite_rom.file_name
                    )
                    game = GamesDB.query_game(game_id=rom.game_id)
                    item = RA_PlaylistItem(
                        path=f"{path_prefix}\\\\{rom.file_name}",
                        label=game.zhcn_title,
                        crc32=rom.crc32,
                        db_name=RA_Configs.lpl_file_name,
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
                path_prefix = str(RA_Configs.xbox_roms_directory).replace("\\", "\\\\")
                for lite_rom in cps1_lite_rom_list:
                    rom = RomsDB.query_rom(
                        rom_crc32=lite_rom.crc32, rom_file_name=lite_rom.file_name
                    )
                    game = GamesDB.query_game(game_id=rom.game_id)
                    item = RA_PlaylistItem(
                        path=f"{path_prefix}\\\\{rom.file_name}",
                        label=game.zhcn_title,
                        crc32=rom.crc32,
                        db_name=RA_Configs.lpl_file_name,
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
