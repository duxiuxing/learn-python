# -- coding: UTF-8 --

import fnmatch
import os

from helper import Helper
from init_global_configs import Init_Global_Configs
from local_configs import LocalConfigs
from logo import Logo
from pathlib import Path
from PIL import Image

DESTINATION_WIDTH = 400
DESTINATION_HEIGHT = 200

if __name__ == "__main__":
    Init_Global_Configs()

    src_dir = None
    while True:
        src_dir = LocalConfigs.repository_directory.joinpath("media\\logo-hd")
        print("\n即将对源文件夹里的 Logo 文件进行重新剪裁")
        print(f"默认源文件夹路径：{src_dir}")
        user_input = input("请确认源文件夹路径，使用默认路径请直接按回车 > ")
        if len(user_input) > 0:
            src_dir = Path(user_input)

        if src_dir.exists() and src_dir.is_dir():
            break
        else:
            print(f"【错误】无效的源文件夹路径：{src_dir}")
            continue

    dst_dir = src_dir.joinpath(f"{DESTINATION_WIDTH}x{DESTINATION_HEIGHT}")
    if not Helper.verify_exist_directory(dst_dir):
        print(f"【错误】无效的目标文件夹路径：{dst_dir}")
        exit()

    dst_png_width = DESTINATION_WIDTH
    dst_png_height = DESTINATION_HEIGHT
    for png_file_name in os.listdir(src_dir):
        if not fnmatch.fnmatch(png_file_name, "*.png"):
            continue

        png_file_path = src_dir.joinpath(png_file_name)
        logo = Logo.resize(
            png_file_path, max_width=dst_png_width, max_height=dst_png_height
        )
        dst_png = Image.new("RGBA", (dst_png_width, dst_png_height), (0, 0, 0, 0))
        x_offset = int((dst_png_width - logo.width) / 2)
        y_offset = int((dst_png_height - logo.height) / 2)
        dst_png.paste(logo, (x_offset, y_offset))
        dst_png_file_path = dst_dir.joinpath(png_file_name)
        if dst_png_file_path.exists() and dst_png_file_path.is_file():
            dst_png_file_path.unlink()
        dst_png.save(dst_png_file_path)
