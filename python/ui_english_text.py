# -- coding: UTF-8 --

import fnmatch
import os

from pathlib import Path


class EnglishLogItem:
    def __init__(self):
        self.ln_index = -1
        self.text = None


class EnglishText:
    @staticmethod
    def log(src_file_path: Path):
        log_item = None
        log_item_list = []

        with open(src_file_path, "r", encoding="utf-8") as src_file:
            line = src_file.readline()
            line_count = 0
            while line:
                index = line.find('UI_TEXT("')
                if index >= 0:
                    log_item = EnglishLogItem()
                    log_item.ln_index = line_count
                    start = index + 9
                    end = line.find('")', start)
                    if end > start:
                        log_item.text = line[start:end]
                        log_item_list.append(log_item)

                line = src_file.readline()
                line_count = line_count + 1
            src_file.close()

        if len(log_item_list) > 0:
            dst_file_path = Path(f"{src_file_path}.ui.txt")
            if dst_file_path.exists() and dst_file_path.is_file():
                dst_file_path.unlink()
            is_first_item = True
            with open(dst_file_path, "w", encoding="utf-8") as dst_file:
                for log_item in log_item_list:
                    if not is_first_item:
                        dst_file.write("\n")
                    dst_file.write(
                        f'Ln={log_item.ln_index + 1}\nEnglish="{log_item.text}"\n'
                    )
                    if is_first_item:
                        is_first_item = False
                dst_file.close()

    @staticmethod
    def check_directory(dir: Path):
        for item_name in os.listdir(dir):
            item_path = dir.joinpath(item_name)
            if item_path.is_dir():
                EnglishText.check_directory(item_path)
            elif item_path.is_file():
                if (
                    fnmatch.fnmatch(item_name, "*.h")
                    or fnmatch.fnmatch(item_name, "*.hh")
                    or fnmatch.fnmatch(item_name, "*.cc")
                    or fnmatch.fnmatch(item_name, "*.ccm")
                ):
                    EnglishText.log(item_path)


if __name__ == "__main__":
    root_dir = Path("D:\\workspace\\github\\duxiuxing\\emu-ex-plus-alpha-cn")

    folder_name_list = [
        "2600.emu",
        "C64.emu",
        "EmuFramework",
        "GBA.emu",
        # "GBC.emu",
        "imagine",
        "Lynx.emu",
        "MD.emu",
        # "MSX.emu",
        "NEO.emu",
        "NES.emu",
        "NGP.emu",
        "PCE.emu",
        "Saturn.emu",
        "Snes9x",
        # "Swan.emu",
    ]
    folder_name_list = ["Snes9x"]
    for folder_name in folder_name_list:
        EnglishText.check_directory(root_dir.joinpath(folder_name))
