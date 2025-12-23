from pathlib import Path, PurePath
import sys
import pandas as pd
import time
import os
import subprocess
import sys
import categorizer

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
        all_content = dirs

        if dirs:
            print("\nDirectories")
            print("------------\n")
            for dir in dirs:
                i += 1
                print(f"  [{i}] {dir}")

        if files:
            files_by_type = categorizer.categorize_files(files)
            # get all content in one list
            print("\nFiles")
            print("-----")

            for key, lst in files_by_type.items():
                print(f"\n>{key}\n")
                all_content += lst
                for item in lst:
                    i += 1
                    print(f"  [{i}] {item}")

        try:
            choice = int(input("\nChoice: "))
            return all_content[choice - 1]
        except Exception:
            print("Error occurred!")
            return None
            
        
        # # get user input
        # try:
        #     choice = int(input("\n\nCHOICE: "))
        #     # check if directory or file
        #     if choice <= len(dirs):
        #         return dirs[choice - 1]
        #     elif choice <= len(dirs) + len(files):
        #         return files[choice - len(dirs) - 1]

        #     else:
        #         return None

        # except Exception:
        #     print("Invalid!")
        #     return None

    
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
    
def get_results(search_term, directory = ""):
    if directory == "":
        docs_dir = get_docs_dir()
        if not docs_dir:
            return []
    else:
        print(f"In Directory {directory}")
        docs_dir = directory

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
    results = []

    start_time = time.perf_counter()

    # get search term from the argument
    if(len(sys.argv) != 2 and len(sys.argv) != 3):
        print(f"Usage: {sys.argv[0]} [file] [directory]")
        return
    elif(len(sys.argv) == 2):
        search_term = sys.argv[1]
        # get results
        results = get_results(search_term)
    elif(len(sys.argv) == 3):
        search_term = sys.argv[1]
        directory = sys.argv[2]
        # get results
        results = get_results(search_term, directory)
    

    
    


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