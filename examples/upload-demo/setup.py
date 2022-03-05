# -*- coding: utf-8 -*-
import setuptools
import os
from dotenv import load_dotenv

load_dotenv(verbose=True)

pip_name = os.environ.get("PIP_NAME")
pip_version = os.environ.get("PIP_VERSION")

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name=pip_name,
    version=pip_version,
    author="lowinli",
    platforms=["any"],
    author_email="lowinli@outlook.com",
    description="这是一个打包的例子",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LowinLi/devpi-docker",
    packages=setuptools.find_packages(),
    install_requires=[
        "numpy>=1.19.4",
    ],
    python_requires=">=3.6",
)
