python -m pip install --upgrade pip setuptools
python -m pip install wheel

python -c "

from setuptools import setup; setup()

" sdist bdist_wheel

pip install ./dist/my_minipack-1.0.0-py3-none-any.whl