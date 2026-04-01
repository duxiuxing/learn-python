# -- coding: UTF-8 --

import os
import shutil
import zlib

from local_configs import LocalConfigs
from pathlib import Path


class Helper:
    @staticmethod
    def compute_crc32(file_path):
        # 计算指定文件的 CRC32
        # Args:
        #     file_path (str): 文件路径，通常是游戏的 ROM 文件
        # Returns:
        #     str: 文件的 CRC32，八位大写十六进制字符串
        with open(file_path, "rb") as file:
            data = file.read()
            crc = zlib.crc32(data)
            crc32 = hex(crc & 0xFFFFFFFF)[2:].upper()
            return crc32.rjust(8, "0")

    @staticmethod
    def verify_exist_directory(folder_path: Path):
        # 判断指定文件夹是否存在，如果不存在则创建该文件夹
        # Args:
        #     folder_path: 待判断的文件夹路径，要求父文件夹必须是存在的
        # Returns:
        #     bool: 如果文件夹存在或创建成功，则返回 True，否则返回 False
        if folder_path.exists():
            return folder_path.is_dir()
        else:
            folder_path.mkdir(parents=True, exist_ok=True)
            return Helper.verify_exist_directory(folder_path)

    @staticmethod
    def verify_exist_directory_ex(folder_path: Path):
        # 判断指定文件夹是否存在，如果不存在则逐级创建
        # Args:
        #     folder_path: 待判断的文件夹路径，如果父文件夹不存在会逐级创建
        # Returns:
        #     bool: 如果文件夹存在或创建成功，则返回 True，否则返回 False
        path = None
        for folder_name in folder_path.parts:
            if path is None:
                path = Path(folder_name)
                if not path.is_dir():
                    return False
            else:
                path = path.joinpath(folder_name)
                if not Helper.verify_exist_directory(path):
                    return False
        return folder_path.is_dir()

    @staticmethod
    def copy_directory(src: Path, dst: Path):
        # 用递归的方式，复制文件夹
        # Args:
        #     src: 源文件夹路径
        #     dst: 目标文件夹路径
        if not Helper.verify_exist_directory_ex(dst):
            print(f"【错误】无效的目标文件夹 {dst}")
            return
        for folder_name in os.listdir(src):
            s = src.joinpath(folder_name)
            d = dst.joinpath(folder_name)
            if s.is_dir():
                Helper.copy_directory(s, d)
            elif not d.exists():
                shutil.copy2(s, d)

    @staticmethod
    def copy_file_if_not_exist(src: Path, dst: Path):
        # 复制文件，如果目标文件已存在则跳过
        # Args:
        #     src: 源文件路径
        #     dst: 目标文件路径，如果父文件夹不存在会逐级创建
        if not Helper.verify_exist_directory_ex(dst.parent):
            print(f"【错误】无效的目标文件 {dst}")
            return
        if not dst.exists():
            if src.exists():
                shutil.copy2(src, dst)
            else:
                print(f"【错误】无效的源文件 {src}")

    @staticmethod
    def copy_file_to_directory(src_file_path: Path, dst_dir: Path):
        # 复制源文件到目标文件夹，如果目标文件已存在则跳过
        # Args:
        #     src_file_path: 源文件路径
        #     dst_dir: 目标文件夹路径，如果文件夹不存在会逐级创建
        dst_file_path = dst_dir.joinpath(src_file_path.name)
        return Helper.copy_file_if_not_exist(src_file_path, dst_file_path)

    @staticmethod
    def remove_region(title):
        left_index = title.find(" (")
        if left_index == -1:
            left_index = title.find("(")
        right_index = title.rfind(")")

        if left_index != -1 and right_index != -1:
            return title.replace(title[left_index : right_index + 1], "")
        else:
            return title

    @staticmethod
    def get_rom_title(rom_name):
        return os.path.splitext(rom_name)[0]

    @staticmethod
    def get_rom_region(rom_name):
        rom_title = os.path.splitext(rom_name)[0]
        left_index = rom_title.find("(")
        right_index = rom_title.find(")")

        if left_index != -1 and right_index != -1:
            rom_region = rom_title[left_index + 1 : right_index]
            if rom_region.upper() == "CHINA" or rom_region == "中":
                return "China"
            elif rom_region.upper() == "EUROPE" or rom_region == "欧":
                return "Europe"
            elif rom_region.upper() == "USA" or rom_region == "美":
                return "USA"
            elif rom_region.upper() == "JAPAN" or rom_region == "日":
                return "Japan"
            else:
                print(f"未知的地区：{rom_region}")
                return rom_region
        else:
            return None

    @staticmethod
    def files_in_letter_folder():
        # 如果 roms 文件夹里有 roms.xml，则返回 False，否则返回 True
        xml_file_path = LocalConfigs.repository_directory().joinpath("roms\\roms.xml")
        if xml_file_path.exists() and xml_file_path.is_file():
            return False
        else:
            return True

    @staticmethod
    def game_id_to_channel_id(game_id):
        dec_num = int(f"0x{game_id}", 16)
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if dec_num == 0:
            return "0000"
        channel_id = ""
        while dec_num > 0:
            remainder = dec_num % 36
            channel_id = digits[remainder] + channel_id
            dec_num //= 36
        return channel_id.rjust(4, "0")
