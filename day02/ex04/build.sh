#!/bin/bash

pip install --upgrade pip setuptools wheel

python -c "

from setuptools import setup; setup()

" sdist bdist_wheel

pip install ./dist/my_minipack-1.0.0-py3-none-any.whl