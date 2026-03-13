# -- coding: UTF-8 --

import os
import subprocess

from helper import Helper
from init_global_configs import Init_Global_Configs
from local_configs import LocalConfigs
from pathlib import Path


if __name__ == "__main__":
    Init_Global_Configs()

    # 调用 wfc_conv.exe 生成 WiiFlow 专用的 Cache 文件（.png 格式转 .wfc 格式）
    # .wfc 格式的文件都存放在 wiiflow\\cache 文件夹里
    wfc_conv_exe_path = LocalConfigs.wfc_conv_exe_path()

    if not wfc_conv_exe_path.exists() or not wfc_conv_exe_path.is_file():
        print(f"【错误】无效的文件 {wfc_conv_exe_path}")
        zip_file_path = LocalConfigs.repository_directory().joinpath(
            "pc-tool\\WFC_conv_0-1.zip"
        )
        print(f"安装文件在 {zip_file_path}")
        exit()

    # wiiflow\\cache
    wiiflow_dir = LocalConfigs.repository_directory().joinpath("wii\\wiiflow")
    wiiflow_cache_dir = wiiflow_dir.joinpath("cache")
    if not Helper.verify_exist_directory_ex(wiiflow_cache_dir):
        print(f"【错误】无效的文件夹 {wiiflow_cache_dir}")
        exit()

    cmd_line = f'"{wfc_conv_exe_path}" "{wiiflow_dir}"'
    print(cmd_line)
    subprocess.call(cmd_line)
