from pathlib import Path
import os
import time

def get_all_files(given_files):
    files = []
    filetypes = []
    try:
        for given in given_files:
            if given.is_file():
                root, extension = os.path.splitext(given)
                # add to list
                files.append(given)
                if extension not in filetypes:
                    filetypes.append(extension)
        return files, filetypes
    except FileNotFoundError:
        print("error!")
        return None

def categorize_files(given_files):
    files, types = get_all_files(given_files)
    all_files = {}
    
    # create dictionary of all files with their filetypes
    for type in types:
        lst = []
        for f in files:
            root, extension = os.path.splitext(f)
            if extension == type:
                lst.append(f)
        all_files[type] = lst
    
    return all_files

def choose_from_list(files):
    # create one list of all the files
    i = 0
    
    all_files = []
    for key, lst in files.items():
        print(f"\n{key}\n")
        all_files += lst
        for item in lst:
            i += 1
            print(f"  [{i}] {item}")

    try:
        choice = int(input("\nChoice: "))
        return all_files[choice - 1]
    except Exception:
        print("Error occurred!")
        return None
