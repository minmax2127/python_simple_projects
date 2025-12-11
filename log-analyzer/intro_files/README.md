Here’s a solid **intermediate-level Python challenge** that tests data structures, algorithms, and clean code design:

---

## 🧩 **Intermediate Python Challenge: Log File Analyzer**

### **Problem**

You are given a text log file where each line follows this format:

```
[timestamp] LEVEL: message
```

Examples:

```
[2025-01-13 12:30:55] INFO: User login successful
[2025-01-13 12:31:02] WARNING: Disk space low
[2025-01-13 12:31:10] ERROR: Failed to save file
```

### **Your Task**

Write a Python function `analyze_logs(filepath)` that returns a dictionary with:

1. **Total number of log entries**
2. **Count of each log level** (`INFO`, `WARNING`, `ERROR`, etc.)
3. **The most recent ERROR message** (or `None` if no errors)
4. **A list of all log messages sorted by timestamp**

### **Requirements**

* Parse timestamps as `datetime` objects.
* Handle malformed lines gracefully (skip them).
* Efficiency matters: the file could be **100MB+**.
* No external libraries besides Python standard library.

### **Example Output**

```python
{
    "total": 15322,
    "levels": {"INFO": 9120, "WARNING": 4200, "ERROR": 2},
    "latest_error": "[2025-01-13 12:31:10] ERROR: Failed to save file",
    "sorted_messages": ["...", "...", "..."]
}
```

---