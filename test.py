import os 
import sys


def create_file(foder_name: str, file_name: str="index.md"):
    if not os.path.exists(foder_name):
        os.mkdir(foder_name)
    try:
        file_name_path = os.path.join(foder_name, file_name)
        with open(file_name_path, 'x') as f:
            print(f"{file_name_path} created Successfully !")
    except FileExistsError:
        print("File already exists")
        sys.exit(1)
        


if __name__ == "__main__":
    for i in range(8,101):
        foldername = f"day{i}"
        create_file(foldername)

