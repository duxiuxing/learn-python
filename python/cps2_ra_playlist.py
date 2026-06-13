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

cps2_rom_file_name_list = [
    # # - 1944 征服世界
    "1944d.zip",
    # # - 19XX 命运否决战
    "19xxd.zip",
    # C - 超强魔法气泡
    "mpang.zip",
    # C - 超级口袋战士
    "sgemf.zip",
    # C - 超级街头霸王2 加速版
    "ssf2t.zip",
    # C - 超级街头霸王2 周年纪念版
    "hsf2.zip",
    # C - 超级街头霸王2 新挑战者
    "ssf2d.zip",
    # C - 超级魔法大作战
    "dimahoo.zip",
    # E - 恶魔战士 午夜斗士
    "dstlk.zip",
    # H - 火星矩阵 超固体射击
    "mmatrix.zip",
    # H - 环保战士
    "ecofghtr.zip",
    # J - 机甲战士 全金属狂潮
    "cybots.zip",
    # J - 街霸方块
    "spf2td.zip",
    # K - 卡普空运动俱乐部
    "csclub.zip",
    # L - 洛克人1 力量之战 (CPS2版)
    "mmancp2u.zip",
    # L - 洛克人2 力量对决
    "megaman2.zip",
    # L - 龙与地下城1 毁灭之塔
    "ddtod.zip",
    # L - 龙与地下城2 暗黑秘影
    "ddsom.zip",
    # M - 漫威对卡普空 超级英雄乱斗
    "mvscud.zip",
    # M - 漫威超级英雄
    "msh.zip",
    # M - 漫威超级英雄对街头霸王
    "mshvsf.zip",
    # N - 能源之岚
    "progear.zip",
    # Q - 千兆之翼
    "gigawing.zip",
    # Q - 雀国志 霸王的采牌
    "jyangoku.zip",
    # S - 少年街霸1 斗士的梦想
    "sfa.zip",
    # S - 少年街霸2
    "sfa2.zip",
    # S - 少年街霸2 Alpha
    "sfz2al.zip",
    # S - 少年街霸3
    "sfa3.zip",
    # S - 摔角霸王2 连环爆裂
    "ringdest.zip",
    # W - 问答七彩梦 虹色町的奇迹
    "qndream.zip",
    # X - X战警 磁场原子人
    "xmcota.zip",
    # X - X战警对街头霸王
    "xmvsf.zip",
    # X - 吸血鬼猎人1 恶魔的复仇
    "nwarr.zip",
    # X - 吸血鬼猎人2 恶魔的复仇
    "vhunt2.zip",
    # X - 恶魔救世主1 吸血鬼之王
    "vsav.zip",
    # X - 恶魔救世主2 吸血鬼之王
    "vsav2.zip",
    # Y - 异形对铁血战士
    "avspu.zip",
    # Y - 益智麻将牌 长江
    "choko.zip",
    # Z - 战斗回路
    "batcir.zip",
    # Z - 智力循环2
    "pzloop2.zip",
    # Z - 装甲战士
    "armwar.zip",
]

if __name__ == "__main__":
    Init_Global_Configs()

    configs = RA_PlaylistConfigs()

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
                for rom_file_name in cps2_rom_file_name_list:
                    rom = RomsDB.query_rom(rom_file_name=rom_file_name)
                    game = GamesDB.query_game(game_id=rom.game_id)
                    item = RA_PlaylistItem(
                        path=f"{RA_Configs.android_roms_directory}/{rom_file_name}",
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
                for rom_file_name in cps2_rom_file_name_list:
                    rom = RomsDB.query_rom(rom_file_name=rom_file_name)
                    game = GamesDB.query_game(game_id=rom.game_id)
                    item = RA_PlaylistItem(
                        path=f"{RA_Configs.ipad_roms_directory}/{rom_file_name}",
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
                for rom_file_name in cps2_rom_file_name_list:
                    rom = RomsDB.query_rom(rom_file_name=rom_file_name)
                    game = GamesDB.query_game(game_id=rom.game_id)
                    item = RA_PlaylistItem(
                        path=f"{RA_Configs.ps3_roms_directory}/{rom_file_name}",
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
                for rom_file_name in cps2_rom_file_name_list:
                    rom = RomsDB.query_rom(rom_file_name=rom_file_name)
                    game = GamesDB.query_game(game_id=rom.game_id)
                    item = RA_PlaylistItem(
                        path=f"{path_prefix}\\\\{rom_file_name}",
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
                for rom_file_name in cps2_rom_file_name_list:
                    rom = RomsDB.query_rom(rom_file_name=rom_file_name)
                    game = GamesDB.query_game(game_id=rom.game_id)
                    item = RA_PlaylistItem(
                        path=f"{path_prefix}\\\\{rom_file_name}",
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
