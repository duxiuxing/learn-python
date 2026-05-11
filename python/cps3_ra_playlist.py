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
        LiteRom("redearth.zip"),
        LiteRom("jojon.zip"),
        LiteRom("jojobaner1.zip"),
        LiteRom("sfiiin.zip"),
        LiteRom("sfiii2.zip"),
        LiteRom("sfiii3.zip"),
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
                configs.rom_path_prefix = "/storage/emulated/0/games/cps3/"
                configs.use_zhcn_title_as_label = True
                configs.png_file_match_rom_file = True

                configs.boxarts_folder = "boxart-stuartc49"
                configs.logos_folder = "logo"
                configs.snaps_folder = "snap"
                configs.titles_folder = "title"
                break
            elif number == 2:
                configs.rom_path_prefix = "~/Documents/RetroArch/arcade/cps3/"
                configs.use_zhcn_title_as_label = True
                configs.png_file_match_rom_file = True

                configs.boxarts_folder = "boxart-stuartc49"
                configs.logos_folder = "logo"
                configs.snaps_folder = "snap"
                configs.titles_folder = "title"
                break
            elif number == 3:
                configs.rom_path_prefix = "/dev_hdd0/game/RETROARCH/USRDIR/arcade/cps3/"
                configs.use_zhcn_title_as_label = True
                configs.png_file_match_rom_file = False

                configs.boxarts_folder = "boxart-stuartc49"
                configs.logos_folder = None
                configs.snaps_folder = "snap"
                configs.titles_folder = "title"
                break
            elif number == 4:
                configs.rom_path_prefix = "X:\\\\arcade\\\\cps3\\\\"
                configs.use_zhcn_title_as_label = True
                configs.png_file_match_rom_file = True

                configs.boxarts_folder = "boxart-stuartc49"
                configs.logos_folder = "logo"
                configs.snaps_folder = "snap"
                configs.titles_folder = "title"
                break
            elif number == 5:
                configs.rom_path_prefix = "E:\\\\arcade\\\\cps3\\\\"
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
