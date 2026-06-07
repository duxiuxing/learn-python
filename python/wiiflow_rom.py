# -- coding: UTF-8 --

from wiiflow_configs import WiiFlow_Configs


class WiiFlow_Rom:
    def __init__(self, game_id, crc32, file_title):
        self.game_id = game_id
        self.crc32 = crc32
        self.file_title = file_title

    def file_name(self):
        return f"{self.file_title}{WiiFlow_Configs.rom_file_extension()}"
