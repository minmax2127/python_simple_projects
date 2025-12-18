from pathlib import Path, PurePosixPath
import sys
import random

'''
Program
- Get path
- Inside the path,
    - Get all files
    - Create directories: [Images, Videos, Codes, Pictures, Text Files, Audio]
    - Move the files to their corresponding directory
'''
FILETYPES = [".png", ".jpg", ".mp4", ".py", ".mp3", ".txt"]

def save_file(dirpath, filename):
    filepath = Path(str(dirpath) + "/" + filename)
    filepath.touch()
    print(f"Created {filename} in {dirpath}")

def get_path(arg_index):
    directory = sys.argv[arg_index]
    
    # get correct directory name
    relative_path = Path(directory)
    path = relative_path.resolve()

    # check if the directory exists
    if path.is_dir():
        return path
    else:
        print(f"{path} does not exist!")
        choice = input(f"\nWould you like to create {path}? [y/n]: ")
        
        if choice == 'y' or choice == 'Y':
            path.mkdir()
            return path
        else:
            print("File generation unsuccessful!")

        

    sys.exit(0)

def create_n_files(dirpath, n):
    for i in range(n):
        extension = random.choice(FILETYPES)
        filename = "file" + str(i) + extension
        save_file(dirpath, filename)
        


def main():
    if(len(sys.argv) != 3):
        print(f"Usage: python3 {sys.argv[0]} [directory-path] [no-of-files]")
        sys.exit(0)

    print(sys.argv)
    path = get_path(1)
    create_n_files(path, int(sys.argv[2]))


    

if __name__ == "__main__":
    main()
    

    

