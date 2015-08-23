"""
This is used in creating a standalone application via py2app

To use this, run:
python setup.py py2app
"""

from setuptools import setup

APP = ['SHAART.py']
DATA_FILES = []
PKGS = ['scikits.audiolab']
OPTIONS = {
    'argv_emulation': True,
    'optimize': True,
    'packages' : PKGS,
    'iconfile':'SHAART.icns'
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
