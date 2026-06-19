# -- coding: UTF-8 --

import os
from pathlib import Path


class LocalConfigs:
    # 本地仓库路径
    repository_directory = None

    # 导出文件夹路径
    export_to_directory = None

    # 导入文件夹路径
    import_from_directory = None

    # 本机 RetroArch 的文件夹路径 
    retroarch_directory = None

    # 本机 7z.exe 的路径
    seven_zip_exe_path = None

    # 本机 wfc_conv.exe 的路径
    wfc_conv_exe_path = None
