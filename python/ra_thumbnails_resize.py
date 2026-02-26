# -- coding: UTF-8 --

import fnmatch
import os

from helper import Helper
from pathlib import Path
from PIL import Image


class RA_ThumbnailsResize:
    WIDTH = 600
    HEIGHT = 600

    def run(self):
        png_dir = Path(
            "D:\\workspace\\github\\R-Sam-1980\\cps3\\thumbnails\\Capcom - CP System III\\Named_Boxarts"
        )
        if not Helper.verify_exist_directory(png_dir):
            print(f"【错误】无效的文件夹 {png_dir}")
            return

        for png_name in os.listdir(png_dir):
            if not fnmatch.fnmatch(png_name, "*.png"):
                continue

            png_path = png_dir.joinpath(png_name)
            png_image = Image.open(png_path)
            if (
                png_image.width != RA_ThumbnailsResize.WIDTH
                or png_image.height != RA_ThumbnailsResize.HEIGHT
            ):
                resized_image = png_image.resize(
                    (RA_ThumbnailsResize.WIDTH, RA_ThumbnailsResize.HEIGHT)
                )
                resized_image.save(png_path)


if __name__ == "__main__":
    RA_ThumbnailsResize().run()
