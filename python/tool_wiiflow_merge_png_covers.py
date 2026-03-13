# -- coding: UTF-8 --

import os

from init_global_configs import Init_Global_Configs
from pathlib import Path
from PIL import Image
from tool_ra_resize_logos import Logo
from wiiflow_configs import WiiFlow_Configs
from wiiflow_resource_file_helper import WiiFlow_ResourceFileHelper


def old_png_cover(rom_file_name):
    png_file_path = WiiFlow_ResourceFileHelper.compute_png_cover_path(rom_file_name)
    if not png_file_path.exists() or not png_file_path.is_file():
        png_file_path = WiiFlow_ResourceFileHelper.png_blank_cover_path()

    if not png_file_path.exists() or not png_file_path.is_file():
        print(f"【错误】无效的文件 {png_file_path}")
        return None

    print(f"准备合成 {rom_file_name} 的全封面")
    print(f"\t选择背景：{png_file_path.name}")
    return Image.open(png_file_path)


def new_png_cover(rom_file_name, png_file_path_dict):
    cover = old_png_cover(rom_file_name)
    if cover is None:
        return

    if cover.width != 1090 or cover.height != 680:
        print(f"【错误】{rom_file_name} 的封面不是标准宽高")
        print(f"\t实际值 = {cover.width}x{cover.height}，预期值 = 1090x680")
        return

    x1 = 515
    x2 = 575

    if "front" in png_file_path_dict.keys():
        front_png_file_path = png_file_path_dict["front"]
        print(f"\t选择封面：{front_png_file_path.name}")
        cover.paste(
            Image.open(front_png_file_path).resize((cover.width - x2, cover.height)),
            (x2, 0),
        )

    if "back" in png_file_path_dict.keys():
        back_png_file_path = png_file_path_dict["back"]
        print(f"\t选择封底：{back_png_file_path.name}")
        cover.paste(
            Image.open(back_png_file_path).resize((x1, cover.height)),
            (0, 0),
        )

    if "logo" in png_file_path_dict.keys():
        logo_png_file_path = png_file_path_dict["logo"]
        print(f"\t选择 Logo：{logo_png_file_path.name}")
        logo = Logo.crop(logo_png_file_path).rotate(-90, expand=True)
        height = int(logo.height * 60 / logo.width)
        overlay = logo.resize((60, height))
        cover.paste(
            overlay,
            (x1, (395 - int(height / 2))),
            overlay,
        )

    new_cover_path = (
        WiiFlow_ResourceFileHelper.png_cover_root_directory().parent.joinpath(
            WiiFlow_ResourceFileHelper.compute_png_cover_path(rom_file_name).name
        )
    )
    if new_cover_path.exists() and new_cover_path.is_file():
        new_cover_path.unlink()
    cover.save(new_cover_path)
    print(f"\t保存全封面：{new_cover_path}")

    wfc_cover_path = WiiFlow_ResourceFileHelper.compute_wfc_cover_path(rom_file_name)
    if wfc_cover_path.exists() and wfc_cover_path.is_file():
        wfc_cover_path.unlink()


if __name__ == "__main__":
    Init_Global_Configs()

    boxcovers_dir = WiiFlow_ResourceFileHelper.png_cover_root_directory().parent
    if not boxcovers_dir.exists() or not boxcovers_dir.is_dir():
        print(f"【警告】无效的文件夹 {boxcovers_dir}")
        exit()

    rom_file_name_to_png_file_path_dict = {}
    for file_name in os.listdir(boxcovers_dir):
        src_path = boxcovers_dir.joinpath(file_name)
        if file_name.endswith("-front.jpg") or file_name.endswith("-front.png"):
            rom_file_name = file_name[:-10]
            if rom_file_name in rom_file_name_to_png_file_path_dict.keys():
                rom_file_name_to_png_file_path_dict[rom_file_name]["front"] = src_path
            else:
                rom_file_name_to_png_file_path_dict[rom_file_name] = {"front": src_path}
        elif file_name.endswith("-back.jpg") or file_name.endswith("-back.png"):
            rom_file_name = file_name[:-9]
            if rom_file_name in rom_file_name_to_png_file_path_dict.keys():
                rom_file_name_to_png_file_path_dict[rom_file_name]["back"] = src_path
            else:
                rom_file_name_to_png_file_path_dict[rom_file_name] = {"back": src_path}
        elif file_name.endswith("-logo.jpg") or file_name.endswith("-logo.png"):
            rom_file_name = file_name[:-9]
            if rom_file_name in rom_file_name_to_png_file_path_dict.keys():
                rom_file_name_to_png_file_path_dict[rom_file_name]["logo"] = src_path
            else:
                rom_file_name_to_png_file_path_dict[rom_file_name] = {"logo": src_path}

    for (
        rom_file_name,
        png_file_path_dict,
    ) in rom_file_name_to_png_file_path_dict.items():
        if WiiFlow_Configs.is_rom_file_name(rom_file_name):
            new_png_cover(rom_file_name, png_file_path_dict)
