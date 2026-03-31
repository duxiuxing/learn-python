# -- coding: UTF-8 --

import fnmatch
import os

from pathlib import Path


class ChineseLogItem:
    def __init__(self):
        self.ln_index = -1
        self.english_text = None
        self.chinese_text = None


class ChineseText:
    @staticmethod
    def log(log_file_path: Path):
        ln_index_to_english_text = {}
        with open(log_file_path, "r", encoding="utf-8") as log_file:
            line = log_file.readline()
            ln_index = -1
            while line:
                if line.startswith("Ln="):
                    ln_index = int(line[3:]) - 1
                elif line.startswith('English="'):
                    ln_index_to_english_text[ln_index] = line[9:-2]
                line = log_file.readline()
            log_file.close()

        log_item = None
        log_item_list = []
        src_file_path = Path(str(log_file_path)[:-7])
        with open(src_file_path, "r", encoding="utf-8") as src_file:
            line = src_file.readline()
            line_count = 0
            while line:
                index = line.find('UI_TEXT("')
                if index >= 0:
                    log_item = ChineseLogItem()
                    log_item.ln_index = line_count
                    start = index + 9
                    end = line.find('")', start)
                    if end > start:
                        log_item.chinese_text = line[start:end]
                        if log_item.ln_index in ln_index_to_english_text.keys():
                            log_item.english_text = ln_index_to_english_text[
                                log_item.ln_index
                            ]
                        else:
                            print(
                                f"【错误】english 分支遗漏 UI_TEXT 标识：{src_file_path}，Ln {log_item.ln_index + 1}"
                            )
                        log_item_list.append(log_item)

                line = src_file.readline()
                line_count = line_count + 1
            src_file.close()

        if len(log_item_list) > 0:
            if log_file_path.exists() and log_file_path.is_file():
                log_file_path.unlink()
            is_first_item = True
            with open(log_file_path, "w", encoding="utf-8") as log_file:
                for log_item in log_item_list:
                    if not is_first_item:
                        log_file.write("\n")
                    log_file.write(
                        f'Ln={log_item.ln_index + 1}\nEnglish="{log_item.english_text}"\nChinese="{log_item.chinese_text}"\n'
                    )
                    if is_first_item:
                        is_first_item = False
                log_file.close()

    @staticmethod
    def check_directory(dir: Path):
        for item_name in os.listdir(dir):
            item_path = dir.joinpath(item_name)
            if item_path.is_dir():
                ChineseText.check_directory(item_path)
            elif item_path.is_file():
                if fnmatch.fnmatch(item_name, "*.ui.txt"):
                    print(item_path)
                    ChineseText.log(item_path)


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
    folder_name_list = ["NES.emu", "Saturn.emu"]
    for folder_name in folder_name_list:
        ChineseText.check_directory(root_dir.joinpath(folder_name))
