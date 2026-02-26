# -- coding: UTF-8 --

import os

from PIL import Image


if __name__ == "__main__":
    src_left = 0
    src_top = 0
    src_right = 0
    src_bottom = 0

    dst_left = 0
    dst_top = 0

    temperature = int(input("输入温度"))
    if temperature < 10:
        print("It is c-old")
    else:
        print("It is hot")

    print(temperature)
