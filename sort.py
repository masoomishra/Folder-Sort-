import os 
import shutil 
from pathlib import Path

#define the path to the downloads folder 
downloads_path = Path.home() / "Downloads"

#explain the categories and their corresponding extensions
categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mov"],
    "Audios": [".mp3"],
    "Scripts": [".py", ".c", ".html"],
    "Others": []
}

def organize_files():
    for item in downloads_path.iterdir():
        if item.is_file():
            file_extension = item.suffix.lower()
            print(f"Processing file: {item.name}, extension: {file_extension}")
            moved = False 
            for category, extensions in categories.items():
                if file_extension in extensions:
                    target_dir = downloads_path / category
                    target_dir.mkdir(parents=True, exist_ok=True)
                    try:
                        print(f"Moving {item} to {target_dir}")
                        shutil.move(str(item), str(target_dir / item.name))
                        moved = True 
                        break
                    except FileNotFoundError:
                        print(f"File '{item}' not found during move operation. Skipping.")
            if not moved:
                other_dir = downloads_path / "Others"
                other_dir.mkdir(parents=True, exist_ok=True)
                try:
                    print(f"Moving {item} to {other_dir}")
                    shutil.move(str(item), str(other_dir / item.name))
                except FileNotFoundError:
                    print(f"File '{item}' not found during move operation. Skipping.")
if __name__ == "__main__":
    organize_files()
    print("Files have been organized!")