#!/usr/bin/env python
from setuptools import setup, find_packages
import os.path

setup(name='CryptoNetwork',
    version='1.0',
    packages=find_packages())

def read_requirements():
    path = os.path.join(os.path.dirname(__file__), "requirements.txt")
    with open(path, "rt") as f:
        requirements = f.read()

    return requirements.splitlines(keepends=False)


setup(install_requires=read_requirements())
