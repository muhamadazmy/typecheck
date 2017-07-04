from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup (
    name='typecheck',
    version='1.0',
    description='Nested type checker for python',
    long_description=long_description,
    url='https://github.com/muhamadazmy/typecheck',
    author='Muhamad Azmy',
    author_email='muhamad.azmy@gmail.com',
    license='Apache 2.0',
    packages=find_packages()
)
