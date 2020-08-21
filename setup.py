"""Setuptools info for the model pip package.

Not yet tested
"""
# https://micropyramid.com/blog/publishing-python-modules-with-pip-via-pypi/
import setuptools  # type:ignore # noqa:

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="restart-model",
    version="2.0.1",
    # this script doesn't exist
    # scripts=["model"],
    author="Restart Partners",
    author_email="lucas@restart.us",  # need a valid email here
    description="COVID-19 decision model tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/restartus/covid-projection",
    packages=setuptools.find_namespace_packages(),
    include_package_data=True,
    install_requires=["streamlit"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
)