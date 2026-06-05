# -- coding: UTF-8 --


class RA_PlaylistItem:
    def __init__(
        self,
        path,
        label,
        crc32,
        db_name,
    ):
        self.path = path
        self.label = label
        self.crc32 = crc32
        self.db_name = db_name
