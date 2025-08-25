# setup.py
from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name='multi-ai-agent',
    version='0.1',
    author='Shahjahan',
    packages=find_packages(),
    install_requires=requirements,
)
# Description for setup.py:
# This is a Python package setup configuration file that defines metadata and dependencies
# for the multi-ai-agent project. It specifies the package name, version, author information,
# and automatically installs required dependencies listed in requirements.txt when the package
# is installed. The setup.py file is essential for making the project installable via pip.

