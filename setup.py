# coding: utf-8

import sys
from setuptools import setup, find_packages

NAME = "external_server"
VERSION = "1.0.1"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion>=2.0.2", "swagger-ui-bundle>=0.0.2", "python_dateutil>=2.6.0"]

setup(
    name=NAME,
    version=VERSION,
    description="GuardAI External Model and Dataset API",
    author_email="guardaisupport@navinfo.eu",
    url="",
    keywords=["OpenAPI", "GuardAI External Model and Dataset API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={"": ["openapi/openapi.yaml"]},
    include_package_data=True,
    entry_points={"console_scripts": ["external_server=external_server.__main__:main"]},
    long_description="""\
    This is the API for the GuardAI External Model and Dataset API.
    """,
)
