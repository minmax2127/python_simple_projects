from pathlib import Path, PurePath
import sys
import pandas as pd
import time
import os
import subprocess
import sys

IGNORE_LIST = [".venv", "venv", ".git", "__pycache__"]

def get_docs_dir():
    docs = Path.home() / "Documents"
    return docs if docs.exists() else None

def is_valid(path, ignore_list = IGNORE_LIST):
    for term in ignore_list:
        if term in str(path):
            return False 
    return True

def separate_dirs_and_files(results):
    dirs = []
    files = []

    for r in results:
        if r.is_dir():
            dirs.append(r)
        elif r.is_file():
            files.append(r)

    return dirs, files

def choose_from_result(results):
    if results:
        dirs, files = separate_dirs_and_files(results)

        i = 0

        if dirs:
            # display directories
            print(f"\nDIRECTORIES ({len(dirs)})\n")
            for i, val in enumerate(dirs):
                print(f"[{i + 1}] {val}")

        if files:
            # display files
            print(f"\nFILES ({len(files)})\n")
            for i, val in enumerate(files):
                print(f"[{i + 1 + len(dirs)}] {val}")

        # get user input
        try:
            choice = int(input("\n\nCHOICE: "))
            # check if directory or file
            if choice <= len(dirs):
                return dirs[choice - 1]
            elif choice <= len(dirs) + len(files):
                return files[choice - len(dirs) - 1]

            else:
                return None

        except Exception:
            print("Invalid!")
            return None

    
    else:
        print("No matching result!")

def copy_to_clipboard(txt):
    # copy to clipboard
    if txt:
        text_to_copy = pd.DataFrame([txt])
        text_to_copy.to_clipboard(index=False, header=False)
        print(f"\n{txt} copied to clipboard!")
    else:
        print("Invalid!")
    
def get_results(search_term):
    docs_dir = get_docs_dir()
    if not docs_dir:
        return []

    results = []
    search_term = search_term.lower()

    for root, dirs, files in os.walk(docs_dir):
        if(is_valid(root)):
            for dir in dirs:
                if is_valid(dir) and search_term in dir:
                    results.append(Path(root) / dir)
            for file in files:
                if is_valid(file) and search_term in file:
                    results.append(Path(root) / file)

    return results


def main():
    print("File Searcher")

    start_time = time.perf_counter()

    # get search term from the argument
    if(len(sys.argv) != 2):
        print(f"Usage: {sys.argv[0]} [file]")
        return
    search_term = sys.argv[1]

    
    # get results
    results = get_results(search_term)

    # Calculate and print the elapsed time
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.4f} seconds")

    # take user choice
    choice = choose_from_result(results)
    
    # copy choice to clipboard
    copy_to_clipboard(choice)



if __name__ == "__main__":
    main()