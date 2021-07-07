import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="fbwisher",
    version="1.2.1",
    description="Automatically send personalized birthday wishes to your friends on facebook",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/shiv-aay/facebook-b-day-wisher",
    author="Shivaay",
    author_email="shivoy4ndixit@gmail.com",
    license="GPLv3",
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["fbwisher"],
    include_package_data=True,
    install_requires=["selenium","chromedriver_autoinstaller"],
    entry_points={
        "console_scripts": [
            "fbwisher=fbwisher.__main__:main",
        ]
    },
)