import random
from datetime import datetime, timedelta
import sys
from pathlib import Path

DIRECTORY = "../log_files"

MIN = 1
MAX = 20000
LEVELS = ["INFO", "WARNING", "ERROR"]

MESSAGES = {
    "INFO": ["User login successful", "Password accepted", "Processing your payment"],
    "WARNING": ["Disk space low", "Password too short", "Too many processes"],
    "ERROR": ["Failed to save file", "Password incorrect", "Login failed"]
}

START_DATE = datetime(2024, 2, 10)

def get_random_datetime(start):
    added_time = random.randrange(100, 30000)
    time = start + timedelta(seconds = added_time)
    if time > datetime.now():
        return None
    return time

def main():

    # create new file
    now = datetime.now()
    filename = f"{now}_log.txt"
    if(len(sys.argv) == 2):
        filename = sys.argv[1]
    N = random.randint(MIN, MAX)

    start = START_DATE
    filename = Path(f"{DIRECTORY}/{filename}")

    try:
        with open(filename, "x") as f:
            for _ in range(N):
                date_time = get_random_datetime(start)
                level = random.choice(LEVELS)
                message = random.choice(MESSAGES[level])
                if date_time != None:
                    f.write(f"[{date_time}] {level}: {message}\n")
                    start = date_time   
            print(f"Logs saved in {filename}!") 
    except FileExistsError:
        print(f"{filename} already exists!")


if __name__ == "__main__":
    main()