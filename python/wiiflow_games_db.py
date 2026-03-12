# -- coding: UTF-8 --

from wiiflow_game import WiiFlow_Game


class WiiFlow_GamesDB:
    __instance = None

    @staticmethod
    def _instance():
        if WiiFlow_GamesDB.__instance is None:
            WiiFlow_GamesDB()
        return WiiFlow_GamesDB.__instance

    def __init__(self):
        WiiFlow_GamesDB.__instance = self
        self._id_to_game = {}

    @staticmethod
    def all_game_ids():
        return WiiFlow_GamesDB._instance()._id_to_game.keys()

    @staticmethod
    def all_games():
        return WiiFlow_GamesDB._instance()._id_to_game.values()

    @staticmethod
    def add_game(game: WiiFlow_Game):
        WiiFlow_GamesDB._instance()._id_to_game[game.id] = game

    @staticmethod
    def query_game(game_id=None, game_title=None) -> WiiFlow_Game:
        games_db = WiiFlow_GamesDB._instance()
        if game_id is not None:
            game = games_db._id_to_game.get(game_id)
            if game is not None:
                return game

        if game_title is not None:
            for game in games_db._id_to_game.values():
                if game_title == game.en_title:
                    return game
                if game_title == game.zhcn_title:
                    return game

        return None
