__author__ = 'godzilla'

import os
from setuptools import setup


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="cli_logging",
    version="0.0.2",
    author="Stanislav Sokolko",
    author_email="s.sokolko@gmail.com",
    description=("Generating loggers from cli params"),
    long_description=read('README'),
    packages=["cli_logging"],
    install_requires=[
    ],
)

