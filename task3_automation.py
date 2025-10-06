import os
import shutil

def move_jpg_files(source_folder, destination_folder):
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    moved_files = 0
    for file in os.listdir(source_folder):
        if file.endswith(".jpg"):
            shutil.move(os.path.join(source_folder, file), os.path.join(destination_folder, file))
            moved_files += 1

    print(f"✅ {moved_files} JPG files moved to {destination_folder}")

if __name__ == "__main__":
    src = input("Enter source folder path: ")
    dest = input("Enter destination folder path: ")
    move_jpg_files(src, dest)
