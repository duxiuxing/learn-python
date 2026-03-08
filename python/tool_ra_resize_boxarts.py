# -- coding: UTF-8 --

import fnmatch
import os

from helper import Helper
from init_global_configs import Init_Global_Configs
from local_configs import LocalConfigs
from pathlib import Path
from PIL import Image


DESTINATION_WIDTH = 600


if __name__ == "__main__":
    Init_Global_Configs()

    src_dir = None
    while True:
        src_dir = LocalConfigs.repository_directory().joinpath("media\\boxart-hd")
        print("\n即将对源文件夹里的封面文件进行重新剪裁")
        print(f"默认源文件夹路径：{src_dir}")
        user_input = input("请确认源文件夹路径，使用默认路径请直接按回车 > ")
        if len(user_input) > 0:
            src_dir = Path(user_input)

        if src_dir.exists() and src_dir.is_dir():
            break
        else:
            print(f"【错误】无效的源文件夹路径：{src_dir}")
            continue

    dst_dir = src_dir.joinpath(f"w{DESTINATION_WIDTH}")
    if not Helper.verify_exist_directory(dst_dir):
        print(f"【错误】无效的目标文件夹路径：{dst_dir}")
        exit()

    for src_png_name in os.listdir(src_dir):
        if not fnmatch.fnmatch(src_png_name, "*.png"):
            continue

        src_png_path = src_dir.joinpath(src_png_name)
        src_png = Image.open(src_png_path)
        if src_png.width < DESTINATION_WIDTH:
            print(
                f"【错误】{src_png.width} x {src_png.height} 的源图片分辨率较低，请使用更高分辨率的图片"
            )
            print(f"\t图片路径：{src_png_path}")
            continue
        elif src_png.width == DESTINATION_WIDTH:
            continue
        else:
            dst_height = int(DESTINATION_WIDTH * src_png.height / src_png.width)
            dst_png = src_png.resize((DESTINATION_WIDTH, dst_height))
            dst_png_path = dst_dir.joinpath(src_png_name)
            if dst_png_path.exists() and dst_png_path.is_file():
                dst_png_path.unlink()
            dst_png.save(dst_png_path)
