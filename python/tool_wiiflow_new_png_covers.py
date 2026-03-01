# -- coding: UTF-8 --

import os

from init_global_configs import Init_Global_Configs
from pathlib import Path
from PIL import Image
from wiiflow_resource_file_helper import WiiFlow_ResourceFileHelper


def old_png_cover(rom_file_name):
    png_file_path = WiiFlow_ResourceFileHelper.compute_png_cover_path(rom_file_name)
    if not png_file_path.exists() or not png_file_path.is_file():
        png_file_path = WiiFlow_ResourceFileHelper.png_blank_cover_path()

    if not png_file_path.exists() or not png_file_path.is_file():
        print(f"【错误】无效的文件 {png_file_path}")
        return None

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
        cover.paste(
            Image.open(png_file_path_dict["front"]).resize(
                (cover.width - x2, cover.height)
            ),
            (x2, 0),
        )

    if "back" in png_file_path_dict.keys():
        cover.paste(
            Image.open(png_file_path_dict["back"]).resize((x1, cover.height)),
            (0, 0),
        )

    new_cover_path = (
        WiiFlow_ResourceFileHelper.png_cover_root_directory().parent.joinpath(
            WiiFlow_ResourceFileHelper.compute_png_cover_path(rom_file_name).name
        )
    )
    if new_cover_path.exists() and new_cover_path.is_file():
        new_cover_path.unlink()
    cover.save(new_cover_path)

    wfc_cover_path = WiiFlow_ResourceFileHelper.compute_wfc_cover_path(rom_file_name)
    if wfc_cover_path.exists() and wfc_cover_path.is_file():
        wfc_cover_path.unlink()


if __name__ == "__main__":
    Init_Global_Configs()

    root_dir = WiiFlow_ResourceFileHelper.png_cover_root_directory()
    if not root_dir.exists() or not root_dir.is_dir():
        print(f"【警告】无效的文件夹 {root_dir}")
        exit()

    rom_file_name_to_png_file_path_dict = {}
    for file_name in os.listdir(root_dir):
        src_path = os.path.join(root_dir, file_name)
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

    for (
        rom_file_name,
        png_file_path_dict,
    ) in rom_file_name_to_png_file_path_dict.items():
        new_png_cover(rom_file_name, png_file_path_dict)
