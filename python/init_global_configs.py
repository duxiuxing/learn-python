# -- coding: UTF-8 --

from local_configs import LocalConfigs
from pathlib import Path
from roms_xml import RomsXML


class Init_Global_Configs:
    def __init__(self):
        # LocalConfigs
        LocalConfigs._repository_directory = Path("I:\\game\\nintendo-wii")
        dir1 = "X:\\"
        LocalConfigs._export_to_directory = Path(dir1)
        LocalConfigs._seven_zip_exe_path = Path("C:\\Program Files\\7-Zip\\7z.exe")
        LocalConfigs._wfc_conv_exe_path = Path(
            "C:\\Program Files\\WFC_conv\\Windows\\wfc_conv.exe"
        )

        RomsXML()


if __name__ == "__main__":
    Init_Global_Configs()

    print("LocalConfigs:")
    print(f"\trepository_directory = {LocalConfigs.repository_directory()}")
    print(f"\texport_to_directory = {LocalConfigs.export_to_directory()}")
    print(f"\tseven_zip_exe_path = {LocalConfigs.seven_zip_exe_path()}")
