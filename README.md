# py_gee_tools
[![Build Status](https://travis-ci.com/elbeejay/py_gee_tools.svg?token=j6zC9aXqWDAY4PjKqpCs&branch=master)](https://travis-ci.com/elbeejay/py_gee_tools)

Helper package to work with the [Python Google Earth Engine API](https://github.com/google/earthengine-api).

For full documentation see: [https://elbeejay.github.io/py_gee_tools](https://elbeejay.github.io/py_gee_tools)

## Installation
The package can be installed in 2 ways:
  1. Cloning the git repository locally and building the package via `python setup.py install`
  2. Installation via `pip`, with `pip install py-gee-tools`
  
This package has been tested on Python 3.6, 3.7 and 3.8

## Module Components 
`landsat_composite.py` : Contains functions to order composite Landsat imagery to Google Drive
 
`cloudmask.py` : Functions from [qgis-earthengine-examples](https://github.com/giswqs/qgis-earthengine-examples) that do some cloud masking

See full documentation for additional information.

## Example
Full example of `landsat_composite.get_one_year` function [here](examples/Ex_SingleYearFunction.py). The brief one-liner is: 

```python
get_one_year(aoi,'Example','KrishnaExample','2018')
```

This example generates an annual composite Landsat 8 image from 2018 of the Krishna River. When visualized in QGIS, the GeoTIFF looks something like this:

<p align="center">
<img src="https://github.com/elbeejay/py_gee_tools/blob/master/examples/KrishnaRiver2018Landsat.png" alt="ExampleComposite" width="300"/>
</p>

## Notes/Misc.
Code still under development. 

Contributions and suggestions are encouraged and welcome.
