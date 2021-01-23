from setuptools import find_packages, setup

setup(
    name='scurri_zipcode',
    packages=find_packages(include=['scurri_zipcode']),
    version='0.1.0',
    description='Python library to validate zip codes in the UK for Scurri interview',
    author='Julieta Colombo',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests'
)