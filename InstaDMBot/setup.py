import os
from io import open

from setuptools import setup

install_requires = ['webdriver_manager', 'selenium']
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

base_dir = os.path.dirname(__file__)

setup(
    name="instadm",
    version='0.0.2',
    author="Umut KAÇAROĞLU",
    author_email="umutkacaroglu@gmail.com",
    url="https://github.com/kacaroglumut/insta-DM-bot",
    description="Instagram bot to send direct messages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=["instadm"],
    zip_safe=False,
    license="GPLv3",
    install_requires=install_requires,
    include_package_data=True,
    classifiers=[
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
    ],
)