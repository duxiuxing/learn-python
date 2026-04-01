# -- coding: UTF-8 --

import os

from game import Game
from helper import Helper
from local_configs import LocalConfigs
from pathlib import Path


class WiiTDB:
    __instance = None

    @staticmethod
    def _instance():
        if WiiTDB.__instance is None:
            WiiTDB()
        return WiiTDB.__instance

    def _parse_en_txt(self):
        txt_file_path = LocalConfigs.repository_directory().joinpath(
            "roms\\wiitdb-en.txt"
        )

        if not txt_file_path.exists() or not txt_file_path.is_file():
            print(f"【错误】无效的文件：{txt_file_path}")
            return

        with open(txt_file_path, "r", encoding="utf-8") as txt_file:
            line = txt_file.readline()
            while line:
                index = line.find(" = ")
                if index == 6:
                    game = Game(
                        id=line[:6],
                        en_title=line[9:-1],
                        zhcn_title=None,
                    )
                    self._id_to_game[game.id] = game
                line = txt_file.readline()
            txt_file.close()

    def _parse_zhcn_txt(self):
        txt_file_path = LocalConfigs.repository_directory().joinpath(
            "roms\\wiitdb-zhcn.txt"
        )

        if not txt_file_path.exists() or not txt_file_path.is_file():
            print(f"【错误】无效的文件：{txt_file_path}")
            return

        with open(txt_file_path, "r", encoding="utf-8") as txt_file:
            line = txt_file.readline()
            while line:
                index = line.find(" = ")
                if index == 6:
                    game_id = line[:6]
                    game = self._id_to_game.get(game_id)
                    if game is None:
                        print(f"【错误】wiitdb-en.txt 里没有配置游戏 ID：{game_id}")
                    else:
                        game.zhcn_title = line[9:-1]
                line = txt_file.readline()
            txt_file.close()

    def __init__(self):
        WiiTDB.__instance = self
        self._id_to_game = {}
        self._parse_en_txt()
        self._parse_zhcn_txt()

    @staticmethod
    def add_game(game: Game):
        WiiTDB._instance()._id_to_game[game.id] = game

    @staticmethod
    def query_game(game_id=None, game_title=None) -> Game:
        wiitdb = WiiTDB._instance()
        if game_id is not None:
            game = wiitdb._id_to_game.get(game_id)
            if game is not None:
                return game

        if game_title is not None:
            for game in wiitdb._id_to_game.values():
                if game_title == game.en_title:
                    return game
                if game_title == game.zhcn_title:
                    return game

        return None
