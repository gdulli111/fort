from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.5'
DESCRIPTION = 'command-line password manager'

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
]

# Setting up
setup(
    name="pyfort",
    version=VERSION,
    packages=find_packages(),
    install_requires=['colorama', 'termcolor', 'cryptography'],
    keywords=['python'],
    entry_points={
        'console_scripts': [
            'fort = pyfort.pyfort:main',
        ],
    },
    classifiers=classifiers,
)
