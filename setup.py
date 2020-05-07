from setuptools import setup

setup(
    name = 'gee_python_tools',
    version = '1.0',
    author = 'Jayaram Hariharan',
    author_email = 'jayaram.hariharan@utexas.edu',
    description = ('Helper functions to work with the Google Earth Engine Python Library'),
    keywords = 'remote sensing, landsat, satellite, Google, Earth Engine, Google Earth Engine, modis',
    url = 'https://github.com/elbeejay/gee_python_tools',
    packages = ['gee_python_tools'],
    long_description = 'See project webpage for details: https://github.com/elbeejay/py_gee_tools',
    classifiers=['Programming Language :: Python :: 3.8'],
    install_requires=['earthengine-api'],
)
