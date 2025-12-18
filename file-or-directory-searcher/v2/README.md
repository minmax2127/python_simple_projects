## Directory Searcher (v2)
A Python program that searches a Linux directory and displays a list of path to files that matches the keyword. The chosen path will be copied to clipboard.

### Revisions
1. Optimized: Reduced computation time (0.78ms -> 0.1ms)
- **os** library instead of pathlib
- using **lambda and custom functions** instead of loop within arrays

2. Categorized: Instead of displaying one list of filepaths, the paths will be **displayed into two categories**: directories and files, which has sub-categories representing the filetype of each file.

