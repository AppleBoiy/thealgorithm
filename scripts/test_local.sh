#!/bin/bash

rm -rf dist build
if [ -d "venv" ]; then
    source venv/bin/activate
else
    echo "Running without virtual environment."
fi

pip install -e . --force-reinstall && python3 -m unittest discover -s tests
