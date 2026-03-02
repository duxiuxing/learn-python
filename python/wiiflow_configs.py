# -- coding: UTF-8 --


class WiiFlow_Configs:
    _plugin_name = None

    @staticmethod
    def plugin_name() -> str:
        return WiiFlow_Configs._plugin_name

    _rom_file_extension = ".zip"

    @staticmethod
    def rom_file_extension() -> str:
        return WiiFlow_Configs._rom_file_extension
