import setuptools

setuptools.setup(
    name='pytimer',
    version='0.0.12',
    description='pytimer is an easy to use timer',
    long_description='context based timer to easily time your code',
    url='https://veltzer.github.io/pytimer',
    download_url='https://github.com/veltzer/pytimer',
    author='Mark Veltzer',
    author_email='mark.veltzer@gmail.com',
    maintainer='Mark Veltzer',
    maintainer_email='mark.veltzer@gmail.com',
    license='MIT',
    platforms=['python3'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
    ],
    keywords='python timing time context manager utility',
    packages=setuptools.find_packages(),
)
