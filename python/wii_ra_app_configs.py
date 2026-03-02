# -- coding: UTF-8 --


class WiiRA_AppConfigs:
    DEVICE_SD = "sd"
    DEVICE_USB = "usb"

    _default_short_description = None

    def __init__(self, long_name: str, short_name: str, rom_file_path_list: list):
        self.long_name = long_name
        self.short_name = short_name
        self.rom_file_path_list = rom_file_path_list
        self.device = None
        self.long_description = None

    def short_description(self) -> str:
        return WiiRA_AppConfigs._default_short_description
