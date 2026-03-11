# -- coding: UTF-8 --

import fnmatch
import re


class WiiFlow_Configs:
    _plugin_name = None

    @staticmethod
    def plugin_name() -> str:
        return WiiFlow_Configs._plugin_name

    _rom_file_extension = ".zip"

    @staticmethod
    def rom_file_extension() -> str:
        return WiiFlow_Configs._rom_file_extension

    _rom_file_renameable = False

    @staticmethod
    def rom_file_renameable() -> bool:
        return WiiFlow_Configs._rom_file_renameable

    _file_name_skip_regex = r"((dis[ck]|tape|side|track)[ _-]([b-l][^a-z]|0*[2-9]|0*[1-9][0-9]))|(^disc2[.]iso$)|(^neogeo[.]zip$)|(^funboot[.]rom$)|(^(ecs|exec|grom)[.]bin$)"

    @staticmethod
    def is_rom_file_name(file_name):
        if not fnmatch.fnmatch(file_name, f"*{WiiFlow_Configs.rom_file_extension()}"):
            return False

        pattern = re.compile(WiiFlow_Configs._file_name_skip_regex)
        if pattern.match(file_name):
            return False
        else:
            return True
