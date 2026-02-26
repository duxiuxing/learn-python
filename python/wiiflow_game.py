# -- coding: UTF-8 --


class WiiFlow_Game:
    def __init__(
        self, name, id, en_title, zhcn_title, developer, publisher, genre, date, players
    ):
        self.name = name
        self.id = id
        self.en_title = en_title
        self.zhcn_title = zhcn_title
        self.developer = developer
        self.publisher = publisher
        self.genre = genre
        self.date = date
        self.players = players
