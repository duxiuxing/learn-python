# -- coding: UTF-8 --

import os
from pathlib import Path


class LocalConfigs:
    _repository_directory = None

    @staticmethod
    def repository_directory() -> Path:
        # 本地仓库路径
        return LocalConfigs._repository_directory

    _export_to_directory = None

    @staticmethod
    def export_to_directory() -> Path:
        # 导出根目录路径
        return LocalConfigs._export_to_directory

    _import_from_directory = None

    @staticmethod
    def import_from_directory() -> Path:
        # 导入根目录路径
        return LocalConfigs._import_from_directory

    _retroarch_directory = None

    @staticmethod
    def retroarch_directory() -> Path:
        return LocalConfigs._retroarch_directory

    _seven_zip_exe_path = None

    @staticmethod
    def seven_zip_exe_path() -> Path:
        # 本机 7z.exe 的路径
        return LocalConfigs._seven_zip_exe_path
