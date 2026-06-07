# -- coding: UTF-8 --

import os

from local_configs import LocalConfigs
from wiiflow_configs import WiiFlow_Configs


class WiiFlow_DeleteGameTdbOffsetBin:
    def run(self):
        # gametdb_offsets.bin 是 WiiFlow 生成的缓存文件，删掉才会重新生成
        plugin_name = WiiFlow_Configs.plugin_name
        gametdb_offsets_bin_path = LocalConfigs.export_to_directory.joinpath(
            f"wiiflow\\plugins_data\\{plugin_name}\\gametdb_offsets.bin",
        )

        if os.path.exists(gametdb_offsets_bin_path):
            os.remove(gametdb_offsets_bin_path)
