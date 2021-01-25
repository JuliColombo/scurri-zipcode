import pathlib

from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='scurri_zipcode',
    packages=find_packages(include=['scurri_zipcode']),
    version='0.1.4',
    long_description=README,
    long_description_content_type="text/markdown",
    description='Python library to validate zip codes in the UK for Scurri interview',
    url="https://github.com/JuliColombo/scurri-zipcode",
    author='Julieta Colombo',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests'
)