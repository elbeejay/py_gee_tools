# cloud masking function for surface reflectance (SR) data.
# From https://github.com/giswqs/qgis-earthengine-examples

import ee

def maskL457(image):
    '''
    Function for masking clouds from a Landsat 4,5, or 7 image.

    Parameters
    ----------
    image : `Landsat Image Object`
        Input Landsat Image Object with the clouds. Should be from a Landsat Surface Reflectance dataset.

    Returns
    -------
    image : `Landsat Image Object`
        The same image with the clouds masked out.

    Example
    -------
    collection = ee.ImageCollection('LANDSAT/LT05/C01/T1_SR') \
        .filterDate('2010-04-01', '2010-07-30')

    composite = collection \
        .map(maskL457) \
        .median()

    Maps the maskL457 function over a collection of Landsat 5 data and takes the median
    '''

    qa = image.select('pixel_qa')
    # If the cloud bit (5) is set and the cloud confidence (7) is high
    # or the cloud shadow bit is set (3), then it's a bad pixel.
    cloud = qa.bitwiseAnd(1 << 5) \
              .And(qa.bitwiseAnd(1 << 7)) \
              .Or(qa.bitwiseAnd(1 << 3))
    # Remove edge pixels that don't occur in all bands
    mask2 = image.mask().reduce(ee.Reducer.min())

    return image.updateMask(cloud.Not()).updateMask(mask2)


def maskL8(image):
    '''
    Function for masking clouds from a Landsat 8 image.

    Parameters
    ----------
    image : `Landsat Image Object`
        Input Landsat Image Object with the clouds. Should be from a Landsat Surface Reflectance dataset.

    Returns
    -------
    image : `Landsat Image Object`
        The same image with the clouds masked out.

    Example
    -------
    collection = ee.ImageCollection('LANDSAT/LC08/C01/T1_SR') \
        .filterDate('2016-01-01', '2016-12-31') \
        .map(maskL8)

    Maps the maskL8 function over a collection of Landsat 8 data and takes the median
    '''

    # Bits 3 and 5 are cloud shadow and cloud, respectively.
    cloudShadowBitMask = 1 << 3
    cloudsBitMask = 1 << 5

    # Get the pixel QA band.
    qa = image.select('pixel_qa')

    # Both flags should be set to zero, indicating clear conditions.
    mask = qa.bitwiseAnd(cloudShadowBitMask).eq(0) \
             .And(qa.bitwiseAnd(cloudsBitMask).eq(0))

    # Return the masked image, scaled to reflectance, without the QA bands.
    return image.updateMask(mask).divide(10000) \
                .select("B[0-9]*") \
                .copyProperties(image, ["system:time_start"])
