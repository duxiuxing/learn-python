# -- coding: UTF-8 --

import fnmatch
import re

from ra_configs import RA_Configs


class WiiFlow_Configs:
    plugin_name = None

    _file_name_skip_regex = r"((dis[ck]|tape|side|track)[ _-]([b-l][^a-z]|0*[2-9]|0*[1-9][0-9]))|(^disc2[.]iso$)|(^neogeo[.]zip$)|(^funboot[.]rom$)|(^(ecs|exec|grom)[.]bin$)"

    @staticmethod
    def is_rom_file_name(file_name):
        if not fnmatch.fnmatch(file_name, f"*{RA_Configs.rom_file_extension}"):
            return False

        pattern = re.compile(WiiFlow_Configs._file_name_skip_regex)
        if pattern.match(file_name):
            return False
        else:
            return True

    website = None
