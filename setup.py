import sys

from pkg_resources import VersionConflict, require
from setuptools import setup, find_packages


with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

try:
    require("setuptools>=38.3")
except VersionConflict:
    print("Error: version of setuptools is too old (<38.3)!")
    sys.exit(1)

setup(
    name="QuantPrimer",
    version="1.0",
    description="Create PCR primers with optimal lengths, tms, gc%s and free energies",
    author="Hafiz Muhammad Hammad",
    author_email="hammad.bs.sbb@pu.edu.pk",
    license="mit",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HafizMHammad/QuantPrimer",
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Environment :: Console",
    ],
    entry_points={"console_scripts": ["primers=primers.main:run"]},
    zip_safe=False,
    python_requires=">=3.0",
)
