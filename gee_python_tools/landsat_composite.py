# Collect annual composite Landsat Imagery for a given Landsat mission

import ee

def get_data(aoi,name,LandsatMission='8'):
    """
    Function to set up a Google Earth Engine task to generate a composite image
    from each year of a Landsat mission given some area of interest (aoi) and
    save the results in a Google Drive folder.

    Parameters
    ----------

    LandsatMission : `str`
        A string of the LandSat Mission number e.g. '4', '5', '7', or '8'

    aoi : `ee.Geometry.Polygon`
        An earth engine polygon geometry defined for a given area of interest

    name : `str`
        The name for the folder to generate in Google Drive
    """

    # Try to initialize EarthEngine, if unable then try to authenticate
    try:
        ee.Initialize()
    except:
        ee.Authenticate()
        ee.Initialize()

    # Define the collection based on the LandsatMission specified.
    # Also set the years over which the mission was run.
    if LandsatMission == '4':
        collection = ee.ImageCollection('LANDSAT/LT04/C01/T1')
        years = [
                 '1983','1984','1985','1986','1987','1988','1989','1990','1991',
                 '1992','1993'
                ]

    elif LandsatMission == '5':
        collection = ee.ImageCollection('LANDSAT/LT05/C01/T1')
        years = [
                 '1992','1993','1994','1995','1996','1997','1998','1999','2000',
                 '2001','2002','2003','2004','2005','2006','2007','2008','2009',
                 '2010','2011'
                ]

    elif LandsatMission == '7':
        collection = ee.ImageCollection('LANDSAT/LE07/C01/T1')
        years = [
                 '1999','2000','2001','2002','2003','2004','2005','2006','2007',
                 '2008','2009','2010','2011','2012','2013','2014','2015','2016',
                 '2017','2018','2019'
                ]

    elif LandsatMission == '8':
        collection = ee.ImageCollection('LANDSAT/LC08/C01/T1')
        years = ['2013','2014','2015','2016','2017','2018','2019']

    else:
        raise ValueError('Invalid LandsatMission specified.')

    # Loop through each year
    for yr in years:
        start = ee.Date(yr+'-01-01')
        end = ee.Date(yr+'-12-31')

        # filter the Landsat image collection using the aoi and filter
        filteredCollection = ee.ImageCollection(collection) \
                                .filterBounds(aoi) \
                                .filterDate(start,end)

        best_img = ee.Algorithms.Landsat.simpleComposite(filteredCollection)

        # Want separate files for the bands of interest
        # I've only wanted the following Landsat bands: Blue, Green,
        # Red, NIR, SWIR1 and SWIR2 could change function to get more/less
        # Depends on the LandSat Mission being used
        if LandsatMission == '4':
            bands = best_img.select('B1','B2','B3','B4','B5','B7')
        elif LandsatMission == '5':
            bands = best_img.select('B1','B2','B3','B4','B5','B7')
        elif LandsatMission == '7':
            bands = best_img.select('B1','B2','B3','B4','B5','B7')
        elif LandsatMission == '8':
            bands = best_img.select('B2','B3','B4','B5','B6','B7')

        # Export to Google Drive
        task = ee.batch.Export.image.toDrive(image=bands,
                                    region=aoi,
                                    description=yr+'_Landsat'+LandsatMission,
                                    folder='RemoteSensing/'+name,
                                    scale=30,
                                    crs='EPSG:4326')

        task.start()
        print('Job sent to Google Earth Engine')




def get_one_year(aoi,foldername,filename,yr=2000):
    """
    Function to set up a Google Earth Engine task to generate a composite image
    from a specified year from the Landsat mission given some area of interest
    (aoi) and save the results in a Google Drive folder. The Landsat mission
    is automatically chosen to match the year specified, for overlapping
    years, the later mission data is used except in the case of Landsat7
    which is avoided when possible.

    Parameters
    ----------

    aoi : `ee.Geometry.Polygon`
        An earth engine polygon geometry defined for a given area of interest

    foldername : `str`
        The name for the folder to generate in Google Drive

    filename : `str`
        Name for the file in addition to the year which will be appeneded

    yr : `str`
        Target year to acquire Landsat composite image. Default = year 2000.
        Min year is 1983 (Landsat4) max is 2019 (Landsat8).

    """

    # Try to initialize EarthEngine, if unable then try to authenticate
    try:
        ee.Initialize()
    except:
        ee.Authenticate()
        ee.Initialize()

    # Define the collection based on the year specified.
    # Landsat4
    if yr in ['1983','1984','1985','1986','1987','1988','1989','1990','1991']:
        LandsatMission = '4'
        collection = ee.ImageCollection('LANDSAT/LT04/C01/T1')

    # Landsat5
    elif yr in ['1992','1993','1994','1995','1996','1997','1998','1999','2000',
                '2001','2002','2003','2004','2005','2006','2007','2008','2009',
                '2010','2011']:
        LandsatMission = '5'
        collection = ee.ImageCollection('LANDSAT/LT05/C01/T1')
        years = [
        '1992','1993','1994','1995','1996','1997','1998','1999','2000','2001',
        '2002','2003','2004','2005','2006','2007','2008','2009','2010','2011'
        ]

    # Landsat7
    elif yr in ['2011','2012']:
        LandsatMission = '7'
        collection = ee.ImageCollection('LANDSAT/LE07/C01/T1')

    # Landsat8
    elif yr in ['2013','2014','2015','2016','2017','2018','2019']:
        LandsatMission = '8'
        collection = ee.ImageCollection('LANDSAT/LC08/C01/T1')

    else:
        raise ValueError('Invalid year specified.')

    # Generate a composite of any images in the AOI over the year specified
    start = ee.Date(yr+'-01-01')
    end = ee.Date(yr+'-12-31')

    # filter the Landsat image collection using the aoi and filter
    filteredCollection = ee.ImageCollection(collection) \
                            .filterBounds(aoi) \
                            .filterDate(start,end)

    best_img = ee.Algorithms.Landsat.simpleComposite(filteredCollection)

    # Want separate files for the bands of interest
    # I've only wanted the following Landsat bands: Blue, Green, Red,
    # NIR, SWIR1 and SWIR2, could change function to get more of them
    # Depends on the LandSat Mission being used
    if LandsatMission == '4':
        bands = best_img.select('B1','B2','B3','B4','B5','B7')
    elif LandsatMission == '5':
        bands = best_img.select('B1','B2','B3','B4','B5','B7')
    elif LandsatMission == '7':
        bands = best_img.select('B1','B2','B3','B4','B5','B7')
    elif LandsatMission == '8':
        bands = best_img.select('B2','B3','B4','B5','B6','B7')

    # Export to Google Drive
    task = ee.batch.Export.image.toDrive(image=bands,
                                region=aoi,
                                description=filename+'_'+yr+'_Landsat'+LandsatMission,
                                folder='RemoteSensing/'+foldername,
                                scale=30,
                                crs='EPSG:4326')

    task.start()
    print('Job sent to Google Earth Engine')



def get_composite(aoi,foldername,filename,startdate,enddate):
    """
    Function to set up a Google Earth Engine task to generate a composite image
    for a specified timeframe within a year of the Landsat mission given some
    area of interest (aoi) and save the results in a Google Drive folder. The
    Landsat mission is automatically chosen to match the year specified, for
    overlapping years, the later mission data is used except in the case of
    Landsat7 which is avoided when possible.

    Parameters
    ----------

    aoi : `ee.Geometry.Polygon`
        An earth engine polygon geometry defined for a given area of interest

    foldername : `str`
        The name for the folder to generate in Google Drive

    filename : `str`
        Name for the file in addition to the year which will be appeneded

    startdate : `str`
        Start date for the composite time window. Format is YYYY-MM-DD.
        Min year is 1983 (Landsat4) max is 2019 (Landsat8).

    enddate : `str`
        End date for the composite time window. Format is YYYY-MM-DD. `enddate`
        must be in the same year as `startdate`.
        Min year is 1983 (Landsat4) max is 2019 (Landsat8).

    """

    # check that dates are within the same year, if not raise error
    if startdate[0:4] != enddate[0:4]:
        raise ValueError('Start and end dates not within the same year.')

    # Try to initialize EarthEngine, if unable then try to authenticate
    try:
        ee.Initialize()
    except:
        ee.Authenticate()
        ee.Initialize()

    # define year
    yr = startdate[0:4]
    # Define the collection based on the year specified.
    # Landsat4
    if yr in ['1983','1984','1985','1986','1987','1988','1989','1990','1991']:
        LandsatMission = '4'
        collection = ee.ImageCollection('LANDSAT/LT04/C01/T1')

    # Landsat5
    elif yr in ['1992','1993','1994','1995','1996','1997','1998','1999','2000',
                '2001','2002','2003','2004','2005','2006','2007','2008','2009',
                '2010','2011']:
        LandsatMission = '5'
        collection = ee.ImageCollection('LANDSAT/LT05/C01/T1')
        years = [
        '1992','1993','1994','1995','1996','1997','1998','1999','2000','2001',
        '2002','2003','2004','2005','2006','2007','2008','2009','2010','2011'
        ]

    # Landsat7
    elif yr in ['2011','2012']:
        LandsatMission = '7'
        collection = ee.ImageCollection('LANDSAT/LE07/C01/T1')

    # Landsat8
    elif yr in ['2013','2014','2015','2016','2017','2018','2019']:
        LandsatMission = '8'
        collection = ee.ImageCollection('LANDSAT/LC08/C01/T1')

    else:
        raise ValueError('Invalid year specified.')

    # Generate a composite of any images in the AOI over the year specified
    start = ee.Date(startdate)
    end = ee.Date(enddate)

    # filter the Landsat image collection using the aoi and filter
    filteredCollection = ee.ImageCollection(collection) \
                            .filterBounds(aoi) \
                            .filterDate(start,end)

    best_img = ee.Algorithms.Landsat.simpleComposite(filteredCollection)

    # Want separate files for the bands of interest
    # I've only wanted the following Landsat bands: Blue, Green, Red,
    # NIR, SWIR1 and SWIR2, could change function to get more of them
    # Depends on the LandSat Mission being used
    if LandsatMission == '4':
        bands = best_img.select('B1','B2','B3','B4','B5','B7')
    elif LandsatMission == '5':
        bands = best_img.select('B1','B2','B3','B4','B5','B7')
    elif LandsatMission == '7':
        bands = best_img.select('B1','B2','B3','B4','B5','B7')
    elif LandsatMission == '8':
        bands = best_img.select('B2','B3','B4','B5','B6','B7')

    # Export to Google Drive
    task = ee.batch.Export.image.toDrive(image=bands,
                                region=aoi,
                                description=filename+'_'+startdate+'_to_'+
                                enddate+'_Landsat'+LandsatMission,
                                folder='RemoteSensing/'+foldername,
                                scale=30,
                                crs='EPSG:4326')

    task.start()
    print('Job sent to Google Earth Engine')
