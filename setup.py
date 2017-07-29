import setuptools

import sys
if not sys.version_info[0] == 3:
    sys.exit("Sorry, only python version 3 is supported")

setuptools.setup(
    name='pytimer',
    version='0.0.12',
    description='pytimer is an easy to use timer',
    long_description='context based timer to easily time your code',
    url='https://veltzer.github.io/pytimer',
    author='Mark Veltzer',
    author_email='mark.veltzer@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
    keywords='python timing time context manager utility',
    packages=setuptools.find_packages(),
)
