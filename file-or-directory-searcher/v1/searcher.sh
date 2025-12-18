#!/bin/bash

echo "File Searcher"

SEARCHER_PY_PATH="/home/maxmin2127/Documents/github/python_simple_projects/file-or-directory-searcher/searcher.py"
VENV_DIR="/home/maxmin2127/Documents/github/python_simple_projects/file-or-directory-searcher/venv"

if [ "$#" -eq 1 ]; then
    search_item=$1
    if [ -f "$VENV_DIR/bin/activate" ]; then
        source "$VENV_DIR/bin/activate"
        python3 "$SEARCHER_PY_PATH" "$search_item"
        deactivate
    else
        echo "Error: Unable to find the activation script in '$VENV_DIR'"
        exit 1
    fi
else
    echo "Usage: $0 [search-item]"
fi