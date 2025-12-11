from pathlib import Path
import sys
import re
from datetime import datetime

def get_log_details(log_str):
    # use regex patterns to get the parts of a log
    patterns = [f"\\[(.*?)\\]", f"\\] (.*?)\\:", r": (.*)"]
    log_details = []

    # each pattern decodes a component of the log
    for p in patterns:
        match = re.search(p, log_str)
        if match:
            extracted_string = match.group(1)
            log_details.append(extracted_string)
        else:
            log_details.append(None)

    # return an object with the log details
    return {
        "log": log_str, 
        "timestamp": datetime.strptime(log_details[0], "%Y-%m-%d %H:%M:%S"), 
        "level": log_details[1], 
        "message": log_details[2], 
    }

def get_level_count(level, logs):
    return sum(l.get("level") == level for l in logs)

def get_sorted_messages(logs):
    sorted_logs = sorted(logs, key=lambda x: x["timestamp"])
    return sorted_logs

def get_latest_error(sorted_logs):
    latest_error = next((log for log in reversed(sorted_logs) if log["level"] == "ERROR"))
    return latest_error

def analyze_logs(filepath):
    # save all logs to a list of log details
    logs = []

    with open(filepath, "r") as f:
        for line in f:
            log = get_log_details(line)
            logs.append(log)

    sorted_logs = get_sorted_messages(logs)

    return {
        "total": len(logs),
        "levels": {
            "INFO": get_level_count("INFO", logs), 
            "WARNING": get_level_count("WARNING", logs), 
            "ERROR": get_level_count("ERROR", logs)
        },
        "latest_error": get_latest_error(sorted_logs)["log"],
        "sorted_messages": [x["log"] for x in sorted_logs]
    }



def main():
    # open file
    filename = "unsorted.txt"
    filepath = Path("log_files/" + filename)
    
    if(not filepath.is_file()):
        print("File does not exist!")
        sys.exit(1)

    summary = analyze_logs(filepath)
    
    # save log_files to same directory as the filepath
    
    outfilepath = Path(str(filepath.parent) + "/summary_of_" + filename)
    
    with open(outfilepath, "w") as f:
        for i, (key, value) in enumerate(summary.items()):
            f.write(f"{key}: ")
            if isinstance(value, list):
                for i, x in enumerate(value):
                    f.write(f"\n#{i + 1}: {x}")
            else:
                f.write(f"{value}\n")
    
    print(f"Summary saved in {outfilepath}!")
    
    
if __name__ == "__main__":
    main()