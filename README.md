# py_gee_tools
[![Build Status](https://travis-ci.com/elbeejay/py_gee_tools.svg?token=j6zC9aXqWDAY4PjKqpCs&branch=master)](https://travis-ci.com/elbeejay/py_gee_tools)

Helper package to work with the [Python Google Earth Engine API](https://github.com/google/earthengine-api). Documentation currently migrating to: [https://elbeejay.github.io/py_gee_tools](https://elbeejay.github.io/py_gee_tools)

## Contents
  - [Dependencies](#dependencies)
  - [Installation](#installation)
  - [Module Components](#module-components)
  - [Examples](#examples)

## Dependencies
  - Access to the [Python Google Earth Engine API](https://developers.google.com/earth-engine/python_install-conda#install_api).
  - [Google Drive](https://www.google.com/drive/) storage for the output files to be placed

## Installation
To install do the following:
  1. Clone the repository: `git clone https://github.com/elbeejay/py_gee_tools`
  2. Change directory into the cloned folder: `cd py_gee_tools`
  3. Build the package: `python setup.py install`
  
This package has been tested on Python 3.6, 3.7 and 3.8

## Module Components 
`landsat_composite.py`
 
  - `landsat_composite.get_data` : Function to set up a Google Earth Engine task to generate an annual composite image for each year of a Landsat mission given some area of interest (aoi) and save the results in a Google Drive folder.
  
  - `landsat_composite.get_one_year` : Function to set up a Google Earth Engine task to generate a composite image from a specified year from the Landsat mission given some area of interest (aoi) and save the output in a Google Drive folder. The Landsat mission is automatically chosen to match the year specified, for overlapping years, the later mission data is used except in the case of Landsat7 which is avoided when possible.

`cloudmask.py` (Functions from [qgis-earthengine-examples](https://github.com/giswqs/qgis-earthengine-examples))
  
  - `cloudmask.maskL457` : Function masks clouds from a Landsat 4, 5, or 7 image
  
  - `cloudmask.maskL8` : Function masks clouds from a Landsat 8 image


Additional information about the functions and their expected input parameters are provided in their docstrings.

## Examples
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
