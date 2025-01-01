#!/bin/bash

if ! command -v coverage &> /dev/null
then
    exit 1
fi

coverage erase

coverage run -m unittest discover

coverage report -m

coverage html
