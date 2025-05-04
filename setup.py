# setup.py
from setuptools import setup, find_packages

setup(
    name='gifmaker',
    version='0.1',
    description='A simple GIF maker from images',
    author='Christian Grundman',
    packages=find_packages(),
    install_requires=[
        'Pillow',
    ],
)