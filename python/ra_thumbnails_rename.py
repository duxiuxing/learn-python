# -- coding: UTF-8 --

import json
import os

from pathlib import Path


class RA_ThumbnailsRename:
    @staticmethod
    def rom_file_title_to_label(lpl_file_path: Path, thumbnails_dir: Path):        
        with open(lpl_file_path, "r", encoding="utf-8") as file:
            items = json.load(file)["items"]
            for item in items:
                rom_file_title = Path(item["path"]).stem
                label = item["label"]
                
                folder_names = ["Named_Boxarts", "Named_Logos", "Named_Snaps", "Named_Titles"]                
                for folder_name in folder_names:
                    folder_path = thumbnails_dir.joinpath(folder_name)
                    old_file_path = folder_path.joinpath(f"{rom_file_title}.png")
                    new_file_path = folder_path.joinpath(f"{label}.png")
                    if old_file_path.exists() and old_file_path.is_file():
                        os.rename(old_file_path, new_file_path)
                    else:
                        print(f"【错误】无效的源文件 {old_file_path}")


    @staticmethod
    def label_to_rom_file_title(lpl_file_path: Path, thumbnails_dir: Path):        
        with open(lpl_file_path, "r", encoding="utf-8") as file:
            items = json.load(file)["items"]
            for item in items:
                rom_file_title = Path(item["path"]).stem
                original_label = item["label"]
                label = original_label.replace(":", "_")
                
                folder_names = ["Named_Boxarts", "Named_Logos", "Named_Snaps", "Named_Titles"]                
                for folder_name in folder_names:
                    folder_path = thumbnails_dir.joinpath(folder_name)
                    if folder_path.exists() and folder_path.is_dir():
                        old_file_path = folder_path.joinpath(f"{label}.png")
                        new_file_path = folder_path.joinpath(f"{rom_file_title}.png")                    
                        if old_file_path.exists() and old_file_path.is_file():
                            os.rename(old_file_path, new_file_path)
                            continue
                        else:
                            print(f"【错误】无效的源文件 {old_file_path}")

if __name__ == "__main__":
    # retroarch_dir = Path("D:\\workspace\\github\\R-Sam-1980\\ra-arcade-release\\ps3")
    # playlist_name = "Capcom - CP System II"
    
    retroarch_dir = Path("X:\\RetroArch-Win64")
    playlist_name = "FBNeo - Arcade Games"
    
    lpl_file_path = retroarch_dir.joinpath(f"playlists\\{playlist_name}.lpl")    
    thumbnails_dir = retroarch_dir.joinpath(f"thumbnails\\{playlist_name}")
    
    # RA_ThumbnailsRename.rom_file_title_to_label(lpl_file_path, thumbnails_dir)
    RA_ThumbnailsRename.label_to_rom_file_title(lpl_file_path, thumbnails_dir)
    