#!/bin/bash

rm -rf dist build

python -m build
twine upload dist/*
