# -- coding: UTF-8 --


class Game:
    def __init__(self, id: str, en_title: str, zhcn_title: str):
        self.id = id
        self.en_title = en_title
        self.zhcn_title = zhcn_title
        self.rom_list = []
