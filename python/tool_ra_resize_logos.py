# -- coding: UTF-8 --

import fnmatch
import os

from helper import Helper
from init_global_configs import Init_Global_Configs
from local_configs import LocalConfigs
from pathlib import Path
from PIL import Image


DESTINATION_WIDTH = 400
DESTINATION_HEIGHT = 200


def check_logo_left(logo, pixel_test):
    for x in range(logo.width):
        for y in range(logo.height):
            if logo.getpixel((x, y)) != pixel_test:
                return x
    return 0


def check_logo_top(logo, pixel_test):
    for y in range(logo.height):
        for x in range(logo.width):
            if logo.getpixel((x, y)) != pixel_test:
                return y
    return 0


def check_logo_right(logo, pixel_test):
    for x_offset in range(1, logo.width + 1):
        for y in range(logo.height):
            if logo.getpixel((logo.width - x_offset, y)) != pixel_test:
                return logo.width - x_offset
    return logo.width - 1


def check_logo_bottom(logo, pixel_test):
    for y_offset in range(1, logo.height + 1):
        for x in range(logo.width):
            if logo.getpixel((x, logo.height - y_offset)) != pixel_test:
                return logo.height - y_offset
    return logo.height - 1


def crop_logo(png_path):
    logo = Image.open(png_path)
    pixel_test = logo.getpixel((0, 0))

    left = check_logo_left(logo, pixel_test)
    top = check_logo_top(logo, pixel_test)
    right = check_logo_right(logo, pixel_test)
    bottom = check_logo_bottom(logo, pixel_test)

    if left == 0 and top == 0 and right == logo.width - 1 and bottom == logo.height - 1:
        return logo

    return logo.crop((left, top, right + 1, bottom + 1))


if __name__ == "__main__":
    Init_Global_Configs()

    src_dir = None
    while True:
        src_dir = LocalConfigs.repository_directory().joinpath("media\\logo-hd")
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

    for src_png_name in os.listdir(src_dir):
        if not fnmatch.fnmatch(src_png_name, "*.png"):
            continue

        src_png_path = src_dir.joinpath(src_png_name)
        src_logo = crop_logo(src_png_path)
        if src_logo.width < DESTINATION_WIDTH and src_logo.height < DESTINATION_HEIGHT:
            print(
                f"【警告】{src_logo.width} x {src_logo.height} 的源 Logo 分辨率较低，建议使用更高分辨率的图片"
            )
            print(f"\t图片路径：{src_png_path}")
        dst_logo_offset_x = 0
        dst_logo_offset_y = 0
        dst_logo = None
        if (src_logo.height * DESTINATION_WIDTH / DESTINATION_HEIGHT) < src_logo.width:
            dst_logo_width = DESTINATION_WIDTH
            dst_logo_height = int(dst_logo_width * src_logo.height / src_logo.width)
            dst_logo = src_logo.resize((dst_logo_width, dst_logo_height))
            dst_logo_offset_y = int((DESTINATION_HEIGHT - dst_logo_height) / 2)
        elif (
            src_logo.height * DESTINATION_WIDTH / DESTINATION_HEIGHT
        ) == src_logo.width:
            dst_logo = src_logo.resize((DESTINATION_WIDTH, DESTINATION_HEIGHT))
        else:
            dst_logo_height = DESTINATION_HEIGHT
            dst_logo_width = int(dst_logo_height * src_logo.width / src_logo.height)
            dst_logo = src_logo.resize((dst_logo_width, dst_logo_height))
            dst_logo_offset_x = int((DESTINATION_WIDTH - dst_logo_width) / 2)

        dst_png = Image.new(
            "RGBA", (DESTINATION_WIDTH, DESTINATION_HEIGHT), (0, 0, 0, 0)
        )
        dst_png.paste(dst_logo, (dst_logo_offset_x, dst_logo_offset_y))
        dst_png_path = dst_dir.joinpath(src_png_name)
        if dst_png_path.exists() and dst_png_path.is_file():
            dst_png_path.unlink()
        dst_png.save(dst_png_path)
