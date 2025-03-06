#!/usr/bin/env python

"""
Call `pip install -e .` to install package locally for testing.
"""

from setuptools import setup

# build command
setup(
    name="records",
    version="0.0.1",
    author="Jamie Woych",
    author_email="jw3943@columbia.edu",
    license="GPLv3",
    description="A package for storing results from GBIF REST query",
    classifiers=["Programming Language :: Python :: 3"],
    entry_points={
        "console_scripts": ["records = records.__main__:main"]
    },
)

