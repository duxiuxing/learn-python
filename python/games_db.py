# -- coding: UTF-8 --

from game import Game


class GamesDB:
    __instance = None

    @staticmethod
    def _instance():
        if GamesDB.__instance is None:
            GamesDB()
        return GamesDB.__instance

    def __init__(self):
        GamesDB.__instance = self
        self._new_id = 0
        self._id_to_game = {}

    @staticmethod
    def new_game_id():
        game_db = GamesDB._instance()
        if game_db._new_id == 0:
            game_db._new_id = len(game_db._id_to_game)
        else:
            game_db._new_id += 1
        return game_db._new_id

    @staticmethod
    def all_game_ids():
        return GamesDB._instance()._id_to_game.keys()

    @staticmethod
    def all_games():
        return GamesDB._instance()._id_to_game.values()

    @staticmethod
    def add_game(game: Game):
        GamesDB._instance()._id_to_game[game.id] = game

    @staticmethod
    def query_game(game_id=None, game_title=None):
        games_db = GamesDB._instance()
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
