# -- coding: UTF-8 --


class Wii_AppConfigs:
    DEVICE_SD = "sd"
    DEVICE_USB = "usb"

    _default_short_description = None

    def __init__(
        self, app_name: str, folder_name: str, rom_file_relative_path_list: list
    ):
        self.app_name = app_name
        self.folder_name = folder_name
        self.rom_file_relative_path_list = rom_file_relative_path_list
        self.device = None
        self.long_description = None

    def short_description(self) -> str:
        return Wii_AppConfigs._default_short_description
