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

cps2_lite_rom_list = [
    # # - 1944 征服世界
    Rom("1944j.zip"),
    # # - 19XX 命运否决战
    Rom("19xxb.zip"),
    # C - 超强魔法气泡
    Rom("mpang.zip"),
    # C - 超级口袋战士
    Rom("sgemf.zip"),
    # C - 超级街头霸王2 加速版
    Rom("ssf2t.zip"),
    # C - 超级街头霸王2 周年纪念版
    Rom("hsf2.zip"),
    # C - 超级街头霸王2 新挑战者
    Rom("ssf2a.zip"),
    # C - 超级魔法大作战
    Rom("dimahoo.zip"),
    # E - 恶魔战士 午夜斗士
    Rom("dstlk.zip"),
    # H - 火星矩阵 超固体射击
    Rom("mmatrix.zip"),
    # H - 环保战士
    Rom("ecofghtr.zip"),
    # J - 机甲战士 全金属狂潮
    Rom("cybots.zip"),
    # J - 街霸方块
    Rom("spf2ta.zip"),
    # K - 卡普空运动俱乐部
    Rom("csclub.zip"),
    # L - 洛克人1 力量之战 (CPS2版)
    Rom("mmancp2u.zip"),
    # L - 洛克人2 力量对决
    Rom("megaman2.zip"),
    # L - 龙与地下城1 毁灭之塔
    Rom("ddtod.zip"),
    # L - 龙与地下城2 暗黑秘影
    Rom("ddsom.zip"),
    # M - 漫威对卡普空 超级英雄乱斗
    Rom("mvsc.zip"),
    # M - 漫威超级英雄
    Rom("msh.zip"),
    # M - 漫威超级英雄对街头霸王
    Rom("mshvsf.zip"),
    # N - 能源之岚
    Rom("progear.zip"),
    # Q - 千兆之翼
    Rom("gigawing.zip"),
    # Q - 雀国志 霸王的采牌
    Rom("jyangoku.zip"),
    # S - 少年街霸1 斗士的梦想
    Rom("sfa.zip"),
    # S - 少年街霸2
    Rom("sfa2.zip"),
    # S - 少年街霸2 Alpha
    Rom("sfz2al.zip"),
    # S - 少年街霸3
    Rom("sfa3.zip"),
    # S - 摔角霸王2 连环爆裂
    Rom("ringdest.zip"),
    # W - 问答七彩梦 虹色町的奇迹
    Rom("qndream.zip"),
    # X - X战警 磁场原子人
    Rom("xmcota.zip"),
    # X - X战警对街头霸王
    Rom("xmvsf.zip"),
    # X - 吸血鬼猎人1 恶魔的复仇
    Rom("nwarr.zip"),
    # X - 吸血鬼猎人2 恶魔的复仇
    Rom("vhunt2.zip"),
    # X - 恶魔救世主1 吸血鬼之王
    Rom("vsav.zip"),
    # X - 恶魔救世主2 吸血鬼之王
    Rom("vsav2.zip"),
    # Y - 异形对铁血战士
    Rom("avsp.zip", "4BFE3F71"),
    # Y - 益智麻将牌 长江
    Rom("choko.zip"),
    # Z - 战斗回路
    Rom("batcir.zip"),
    # Z - 智力循环2
    Rom("pzloop2.zip"),
    # Z - 装甲战士
    Rom("armwar.zip"),
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
                for lite_rom in cps2_lite_rom_list:
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
                for lite_rom in cps2_lite_rom_list:
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
                for lite_rom in cps2_lite_rom_list:
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
                for lite_rom in cps2_lite_rom_list:
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
                for lite_rom in cps2_lite_rom_list:
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
