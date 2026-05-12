# -- coding: UTF-8 --

from init_global_configs import Init_Global_Configs
from local_configs import LocalConfigs
from pathlib import Path
from ra_playlist import LiteRom
from ra_playlist import RA_Playlist
from ra_playlist_config import RA_PlaylistConfig

if __name__ == "__main__":
    Init_Global_Configs()

    lite_rom_list = [
        # # - 1941 反击战
        LiteRom("1941.zip"),
        # C - 出击飞龙
        LiteRom("strider.zip"),
        # C - 惩罚者
        LiteRom("punisher.zip"),
        # C - 雌虎战机
        LiteRom("cawing.zip"),
        # D - 大魔界村
        LiteRom("ghouls.zip"),
        # J - 街头霸王2 四大天王
        LiteRom("sf2ce.zip"),
        # J - 街头霸王2 天下斗士
        LiteRom("sf2.zip"),
        # J - 街头霸王2 战斗宣言
        LiteRom("sf2hf.zip"),
        # K - 快打旋风
        LiteRom("ffight.zip"),
        # K - 恐龙快打
        LiteRom("dino.zip"),
        # L - 洛克人1 力量之战 (CPS1版)
        LiteRom("megaman.zip"),
        # L - 龙之迷题
        LiteRom("qad.zip"),
        # L - 龙王战士
        LiteRom("kod.zip"),
        # M - 冒险问答 卡普空世界2
        LiteRom("cworld2j.zip"),
        # M - 名将
        LiteRom("captcomm.zip"),
        # M - 梦幻冒险
        LiteRom("nemo.zip"),
        # M - 魔法剑 英雄的幻想
        LiteRom("msword.zip"),
        # M - 魔法方块
        LiteRom("pnickj.zip"),
        # M - 魔鬼气泡3
        LiteRom("pang3.zip"),
        # Q - 奇迹三世界
        LiteRom("3wonders.zip"),
        # S - 双麒儿
        LiteRom("mtwins.zip"),
        # S - 失落的世界
        LiteRom("forgottnu.zip"),
        # S - 少年街霸1
        LiteRom("sfzch.zip"),
        # S - 摔角霸王1
        LiteRom("slammast.zip"),
        # S - 摔角霸王1 最终之战
        LiteRom("mbombrd.zip"),
        # T - 吞食天地1 王朝战争
        LiteRom("dynwar.zip"),
        # T - 吞食天地2 赤壁之战
        LiteRom("wof.zip"),
        # W - 威洛之旅
        LiteRom("willowj.zip"),
        # W - 威虎战机 雷暴行动
        LiteRom("varth.zip"),
        # W - 问答信长之野望2 全国版
        LiteRom("qtono2j.zip"),
        # Y - 圆桌骑士
        LiteRom("knights.zip"),
        # Z - 战区88
        LiteRom("unsquad.zip"),
        # Z - 战场之狼2
        LiteRom("mercs.zip"),
    ]
    configs = RA_PlaylistConfig(lite_rom_list)

    while True:
        export_to_dir = LocalConfigs.export_to_directory()
        print(
            f"\n即将导出列表和缩略图到目标文件夹\n默认目标文件夹路径：{export_to_dir}"
        )
        user_input = input("请确认目标文件夹路径，使用默认路径请直接按回车 > ")
        if len(user_input) > 0:
            export_to_dir = Path(user_input)

        if export_to_dir.exists() and export_to_dir.is_dir():
            LocalConfigs._export_to_directory = export_to_dir
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
                configs.rom_path_prefix = "/storage/emulated/0/arcade/cps1/"
                configs.use_zhcn_title_as_label = True
                configs.png_file_match_rom_file = True

                configs.boxarts_folder = "boxart-stuartc49"
                configs.logos_folder = "logo"
                configs.snaps_folder = "snap"
                configs.titles_folder = "title"
                break
            elif number == 2:
                configs.rom_path_prefix = "~/Documents/RetroArch/arcade/cps1/"
                configs.use_zhcn_title_as_label = True
                configs.png_file_match_rom_file = True

                configs.boxarts_folder = "boxart-stuartc49"
                configs.logos_folder = "logo"
                configs.snaps_folder = "snap"
                configs.titles_folder = "title"
                break
            elif number == 3:
                configs.rom_path_prefix = "/dev_hdd0/game/RETROARCH/USRDIR/arcade/cps1/"
                configs.use_zhcn_title_as_label = True
                configs.png_file_match_rom_file = False

                configs.boxarts_folder = "boxart-stuartc49"
                configs.logos_folder = None
                configs.snaps_folder = "snap"
                configs.titles_folder = "title"
                break
            elif number == 4:
                configs.rom_path_prefix = "X:\\\\arcade\\\\cps1\\\\"
                configs.use_zhcn_title_as_label = True
                configs.png_file_match_rom_file = True

                configs.boxarts_folder = "boxart-stuartc49"
                configs.logos_folder = "logo"
                configs.snaps_folder = "snap"
                configs.titles_folder = "title"
                break
            elif number == 5:
                configs.rom_path_prefix = "E:\\\\arcade\\\\cps1\\\\"
                configs.use_zhcn_title_as_label = True
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
