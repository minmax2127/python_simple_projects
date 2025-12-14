from pathlib import Path, PurePath
import sys
import subprocess
import pandas as pd

base_dir = Path("/home/maxmin2127/Documents")
ignore_list = [".venv", "venv", ".git"]

def search_directory(search_term):
    #search_results = []
    results = base_dir.rglob("*")

    # remove directories to be ignored
    for item in ignore_list:
        results = [r for r in results if item not in r.parts]
    
    # search all files and directory for matching results
    results = [r for r in results if r.is_dir() or r.is_file()]
    matched_results = [r for r in results if search_term in r.name]

    return matched_results

def choose_from_result(results):

    for i, val in enumerate(results):
        print(f" [{i + 1}] {val}")
    
    try:
        choice = int(input("Choice: "))
        if choice <= len(results):
            return results[choice - 1]
        else:
            print("Invalid answer!")
            return None
    except Exception:
        print("Invalid!")
        return None


def main():
    # get search term from the argument
    if(len(sys.argv) != 2):
        print(f"Usage: {sys.argv[0]} [file]")
        return
    search_term = sys.argv[1]

    # get results
    results = search_directory(search_term)

    # display results
    if len(results) == 0:
        print("No matching result!")
        return
    
    # make user choose a directory
    choice = None
    while choice == None:
        choice = choose_from_result(results)

    # copy to clipboard
    text_to_copy = pd.DataFrame([choice])
    text_to_copy.to_clipboard(index=False, header=False)
    print(f"{choice} copied to clipboard!")
    

if __name__ == "__main__":
    main()