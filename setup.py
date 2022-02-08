import pathlib
from setuptools import setup
from pybind11.setup_helpers import Pybind11Extension

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE/"README.md").read_text()

ext_modules = [
        Pybind11Extension("disam", ["src/_sample_data.cpp"])
        ]

setup(
        name="disam",
        version="1.0.0",
        description="Implements sampling from disk for large datasets",
        url="https://github.com/Nadr0jj/disam",
        install_requires=["numpy", "pybind11"],
        ext_modules=ext_modules)


        
