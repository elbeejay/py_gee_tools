import ee
from gee_python_tools.landsat_composite import get_one_year

# init google earthengine
try:
    ee.Initialize()
except:
    ee.Authenticate()
    ee.Initialize()

# define the area of interest
aoi = ee.Geometry.Polygon([[
        [80.67398071289062,
        15.638906863563108],
        [81.18484497070312,
        15.638906863563108],
        [81.18484497070312,
        16.1381772221918],
        [80.67398071289062,
        16.1381772221918]
        ]])

# run the get_one_year function
    # gets the 2018 Landsat composite for the area of interest (aoi)
    # Saves it to a folder called 'Example' in Google Drive
    # File name becomes 'KrishnaExample.tif'
get_one_year(aoi,'Example','KrishnaExample','2018')
