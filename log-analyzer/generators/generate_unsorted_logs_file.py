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

def get_random_datetime(start, end):
    delta = end - start
    delta_seconds = int(delta.total_seconds())
    random_seconds = random.randrange(delta_seconds)

    generated_datetime = start + timedelta(seconds = random_seconds)

    if generated_datetime > end:
        return None
    return generated_datetime

def main():

    # create new file
    now = datetime.now()
    filename = f"{now}_log.txt"
    if(len(sys.argv) == 2):
        filename = sys.argv[1]
    N = random.randint(MIN, MAX)

    
    filename = Path(f"{DIRECTORY}/{filename}")


    try:
        with open(filename, "x") as f:
            for _ in range(N):
                date_time = get_random_datetime(START_DATE, now)
                level = random.choice(LEVELS)
                message = random.choice(MESSAGES[level])
                if date_time != None:
                    f.write(f"[{date_time}] {level}: {message}\n")
            print(f"Logs saved in {filename}!") 
    except FileExistsError:
        print(f"{filename} already exists!")


if __name__ == "__main__":
    main()