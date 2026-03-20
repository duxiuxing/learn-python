# -- coding: UTF-8 --

import os

from init_global_configs import Init_Global_Configs
from local_configs import LocalConfigs
from pathlib import Path
from PIL import Image
from tool_ra_resize_logos import Logo
from wiiflow_configs import WiiFlow_Configs
from wiiflow_resource_file_helper import WiiFlow_ResourceFileHelper


class MovieBoxCover:
    WIDTH = 1090
    HEIGHT = 680


def merge(movie_file_name):
    print(f"准备合成 {movie_file_name} 的全封面")
    src_dir = LocalConfigs.repository_directory().joinpath(
        "boxcovers-hd", Path(movie_file_name).stem
    )
    if not src_dir.exists() or not src_dir.is_dir():
        print(f"【错误】无效的文件夹 {src_dir}")
        return

    cover = Image.new("RGBA", (MovieBoxCover.WIDTH, MovieBoxCover.HEIGHT), (0, 0, 0, 0))

    x1 = 514
    x2 = 576

    front_png_file_path = src_dir.joinpath(f"{movie_file_name}-front.png")
    if front_png_file_path.exists() and front_png_file_path.is_file():
        print(f"\t选择封面：{front_png_file_path.name}")
        cover.paste(
            Image.open(front_png_file_path).resize((cover.width - x2, cover.height)),
            (x2, 0),
        )

    back_png_file_path = src_dir.joinpath(f"{movie_file_name}-back.png")
    if back_png_file_path.exists() and back_png_file_path.is_file():
        print(f"\t选择封底：{back_png_file_path.name}")
        cover.paste(
            Image.open(back_png_file_path).resize((x1, cover.height)),
            (0, 0),
        )

    spin_png_file_path = src_dir.joinpath(f"{movie_file_name}-spin.png")
    if spin_png_file_path.exists() and spin_png_file_path.is_file():
        print(f"\t选择盒脊：{spin_png_file_path.name}")
        cover.paste(
            Image.open(spin_png_file_path).resize((x2 - x1, cover.height)),
            (x1, 0),
        )

    head_png_file_path = src_dir.joinpath(f"{movie_file_name}-head.png")
    if head_png_file_path.exists() and head_png_file_path.is_file():
        print(f"\t选择头像：{head_png_file_path.name}")
        cover.paste(
            Image.open(head_png_file_path).resize((x2 - x1, 164)),
            (x1, 0),
        )

    logo_png_file_path = src_dir.joinpath(f"{movie_file_name}-logo.png")
    if logo_png_file_path.exists() and logo_png_file_path.is_file():
        print(f"\t选择 Logo：{logo_png_file_path.name}")
        logo = Logo.crop(logo_png_file_path).rotate(-90, expand=True)
        offset_x = 6
        width = x2 - x1 - offset_x - offset_x
        height = int(logo.height * width / logo.width)
        overlay = logo.resize((width, height))
        center_y = int((610 + 164) / 2)
        cover.paste(
            overlay,
            (x1 + offset_x, (center_y - int(height / 2))),
            overlay,
        )

    dst_cover_path = LocalConfigs.repository_directory().joinpath(
        f"{movie_file_name}.png"
    )
    if dst_cover_path.exists() and dst_cover_path.is_file():
        dst_cover_path.unlink()
    cover.save(dst_cover_path)
    print(f"\t保存全封面：{dst_cover_path}")

    wfc_cover_path = LocalConfigs.repository_directory().joinpath(
        "wiiflow\\cache",
        f"{WiiFlow_Configs.plugin_name()}\\{movie_file_name}.wfc",
    )
    if wfc_cover_path.exists() and wfc_cover_path.is_file():
        print(f"\t删除旧封面：{wfc_cover_path.name}")
        wfc_cover_path.unlink()


def cut_then_merge(movie_file_name, front_width, back_width, spin_left, spin_right):
    print(f"准备合成 {movie_file_name} 的全封面")
    src_cover_path = LocalConfigs.repository_directory().joinpath(
        "boxcovers-hd", f"{movie_file_name}.png"
    )
    if not src_cover_path.exists() or not src_cover_path.is_file():
        print(f"【错误】无效的文件 {src_cover_path}")
        return

    if spin_left < back_width:
        print(
            f"【错误】封底和盒脊的区域重合：back_width={back_width}, spin_left={spin_left}"
        )
        return

    src_cover = Image.open(src_cover_path)
    if spin_right > (src_cover.width - front_width):
        print(
            f"【错误】封面和盒脊的区域重合：front_width={front_width}, 起始x坐标={src_cover.width - front_width}, spin_right={spin_right}"
        )
        return

    dst_cover = Image.new(
        "RGBA", (MovieBoxCover.WIDTH, MovieBoxCover.HEIGHT), (0, 0, 0, 0)
    )

    x1 = 514
    x2 = 576

    front = src_cover.crop(
        (src_cover.width - front_width, 0, src_cover.width, src_cover.height)
    )
    print(
        f"\t截取封面，x坐标区间：[{src_cover.width - front_width}, {src_cover.width})"
    )
    dst_cover.paste(
        front.resize((dst_cover.width - x2, dst_cover.height)),
        (x2, 0),
    )

    back = src_cover.crop((0, 0, back_width, src_cover.height))
    print(f"\t截取封底，x坐标区间：[0, {back_width})")
    dst_cover.paste(
        back.resize((x1, dst_cover.height)),
        (0, 0),
    )

    spin = src_cover.crop((spin_left, 0, spin_right, src_cover.height))
    print(f"\t截取盒脊，x坐标区间：[{spin_left}, {spin_right})")
    dst_cover.paste(
        spin.resize((x2 - x1, dst_cover.height)),
        (x1, 0),
    )

    dst_cover_path = LocalConfigs.repository_directory().joinpath(
        f"{movie_file_name}.png"
    )
    if dst_cover_path.exists() and dst_cover_path.is_file():
        dst_cover_path.unlink()
    dst_cover.save(dst_cover_path)
    print(f"\t保存全封面：{dst_cover_path}")

    wfc_cover_path = LocalConfigs.repository_directory().joinpath(
        "wiiflow\\cache",
        f"{WiiFlow_Configs.plugin_name()}\\{movie_file_name}.wfc",
    )
    if wfc_cover_path.exists() and wfc_cover_path.is_file():
        print(f"\t删除旧封面：{wfc_cover_path.name}")
        wfc_cover_path.unlink()


if __name__ == "__main__":
    Init_Global_Configs()

    """
    # merge("# - 92应召女郎 (1992).avi")
    # merge("B - 变相怪杰 (1994).rmvb")
    # merge("C - 重返十七岁 (2009).rmvb")
    # merge("F - 富贵黄金屋 (1992).rmvb")
    # merge("H - 黑心鬼 (1988).rmvb")
    # merge("J - 绝桥智多星 (1990).mp4")
    # merge("W - 我是谁 (1998).rmvb")
    # merge("Z - 至尊计状元才 (1990).rmvb")

    cut_then_merge("B - 变相怪杰2 面具之子 (2005).rmvb", 621, 625, 625, 719)
    cut_then_merge("K - 空军一号 (1997).rmvb", 450, 450, 450, 500)
    cut_then_merge("S - 史密斯夫妇 (2005).rmvb", 706, 707, 707, 783)
    cut_then_merge("Z - 蜘蛛侠 (2002).rmvb", 607, 607, 607, 673)
    cut_then_merge("Z - 蜘蛛侠2 (2004).rmvb", 451, 450, 450, 499)
    cut_then_merge("S - 双瞳 (2002).mkv", 706, 707, 709, 785)
    cut_then_merge("Z - 专钓大鳄 (1989).mkv", 488, 486, 486, 536)
    cut_then_merge(
        "",
        front_width=,
        back_width=,
        spin_left=,
        spin_right=,
    )
    """
