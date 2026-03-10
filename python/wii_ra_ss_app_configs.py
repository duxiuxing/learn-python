# -- coding: UTF-8 --

from pathlib import Path
from wii_ra_app_configs import WiiRA_AppConfigs


class WiiRA_SS_AppConfigs:
    def __init__(self, app_name: str, folder_name: str):
        self.app_name = app_name
        self.folder_name = folder_name
        self.device = None
        self.long_description = None

    def short_description(self) -> str:
        return WiiRA_AppConfigs._default_short_description
