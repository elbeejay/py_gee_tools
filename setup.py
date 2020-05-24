from setuptools import setup

setup(
    name = 'py_gee_tools',
    version = '0.1',
    author = 'Jayaram Hariharan',
    author_email = 'jayaram.hariharan@utexas.edu',
    description = ('Helper package to work with the Google Earth Engine Python Library'),
    keywords = ['remote sensing, landsat, satellite, Google, Earth Engine, Google Earth Engine, modis', 'sentinel', 'sentinel-2'],
    url = 'https://github.com/elbeejay/py_gee_tools',
    packages = ['gee_python_tools'],
    long_description = 'See project documentation for details: https://elbeejay.github.io/py_gee_tools',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: Apache Software License',
    ],
    python_requires='>=3.6',
    install_requires=['earthengine-api'],
)
