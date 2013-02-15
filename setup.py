#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    bigimg
    ~~~~~~
"""

from distutils.core import setup

setup(
    name='bigimg',
    version='0.0.2',
    url='http://github.com/stephenbalaban/bigimp',
    author='Stephen Balaban',
    author_email='stephen@stephenbalaban.com',
    packages=[
        'bigimg',
        'test',
        ],
    platforms='any',
    scripts=['scripts/bigimg'],
    license='LICENSE',
    install_requires=[
        'scipy',
        'numpy',
        ],
    description="",
    long_description=open('README.md').read(),
)
