import os
from setuptools import setup, find_packages


def get_version():
    filename = os.path.join(os.path.dirname(__file__), 'PyBundle', '_version.py')
    with open(filename, 'rb') as fp:
        return fp.read().decode('utf8').split('=')[1].strip(" \n'")

setup(
    name='PyBundle',
    version=get_version(),
    packages=find_packages(),
    url='https://github.com/mrstephenneal/PyBundle',
    license='MIT',
    author='Stephen Neal',
    author_email='stephen@stephenneal.net',
    description='Wrapper functions for adjusting paths in executable builds'
)
