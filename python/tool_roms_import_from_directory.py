# -- coding: UTF-8 --

import fnmatch
import os
import shutil

from game import Game
from games_db import GamesDB
from helper import Helper
from init_global_configs import Init_Global_Configs
from local_configs import LocalConfigs
from pathlib import Path
from wiitdb import WiiTDB


def check_file(file_path: Path):
    if not fnmatch.fnmatch(file_path.name, "*.wbfs"):
        return False

    game_id = file_path.stem
    game = GamesDB.query_game(game_id=game_id)
    if game is not None:
        print(f"【提示】{game_id}={game.en_title} 无需导入：{file_path}")
        return False

    game = WiiTDB.query_game(game_id=game_id)
    if game is None:
        print(f"【错误】wiitdb-en.txt 里没有配置游戏 ID：{file_path}")
        return False

    GamesDB.add_game(game)
    print(
        f'    <Game id="{game.id}"\n'
        f'        en_title="{game.en_title}"\n'
        f'        zhcn_title="{game.zhcn_title}"\n'
        "    />"
    )

    src_dir = file_path.parent
    letter = game.en_title.upper()[0]
    if letter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        letter = "#"
    dst_dir = LocalConfigs.repository_directory().joinpath(
        f"roms\\{letter}\\{src_dir.name}"
    )
    Helper.verify_exist_directory(dst_dir.parent)

    print(f"移动文件夹：\n\t源文件夹：{src_dir}\n\t目标文件夹：{dst_dir}")
    shutil.move(src_dir, dst_dir)
    return True


def check_directory(dir: Path):
    for item_name in os.listdir(dir):
        item_path = dir.joinpath(item_name)
        if item_path.is_dir():
            check_directory(item_path)
        elif item_path.is_file():
            if check_file(item_path):
                break
        else:
            print(f"【错误】未知的路径：{item_path}")


if __name__ == "__main__":
    Init_Global_Configs()

    LocalConfigs._import_from_directory = Path("I:\\Wii游戏整理\\运动游戏 健身\\wbfs")

    import_from_dir = None
    while True:
        import_from_dir = LocalConfigs.import_from_directory()
        print("\n即将导入源文件夹里的 ROM 文件")
        print(f"默认源文件夹路径：{import_from_dir}")
        user_input = input("请确认源文件夹路径，使用默认路径请直接按回车 > ")
        if len(user_input) > 0:
            import_from_dir = Path(user_input)

        if import_from_dir.exists() and import_from_dir.is_dir():
            break
        else:
            print(f"【错误】无效的源文件夹路径：{import_from_dir}")
            continue

    check_directory(import_from_dir)
