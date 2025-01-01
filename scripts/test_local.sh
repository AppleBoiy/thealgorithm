#!/bin/bash

rm -rf dist build
# check venv activate or not
if [ -d "venv" ] && ! [ -z "$VIRTUAL_ENV" ]; then
    source venv/bin/activate
else
    echo "Running without virtual environment."
fi

pip install -e . --force-reinstall && python3 -m unittest discover -s tests
