'''CONSTANTS'''
ALL_MONTHS = [
        "01", "02", "03",
        "04", "05", "06",
        "07", "08", "09",
        "10", "11", "12"
    ]

ALL_DAYS = [
        "01", "02", "03",
        "04", "05", "06",
        "07", "08", "09",
        "10", "11", "12",
        "13", "14", "15",
        "16", "17", "18",
        "19", "20", "21",
        "22", "23", "24",
        "25", "26", "27",
        "28", "29", "30",
        "31"
    ]

ALL_HOURS = [
        "00:00", "01:00", "02:00",
        "03:00", "04:00", "05:00",
        "06:00", "07:00", "08:00",
        "09:00", "10:00", "11:00",
        "12:00", "13:00", "14:00",
        "15:00", "16:00", "17:00",
        "18:00", "19:00", "20:00",
        "21:00", "22:00", "23:00"
    ]

ERA5_LAND = 'reanalysis-era5-single-levels'
'''CDS api request'''
'''example: 10m u,v wind'''


dataset = ERA5_LAND
request = {
    "product_type": ["reanalysis"],
    "variable": [
        "10m_u_component_of_wind",
        "10m_v_component_of_wind"
    ],
    "year": ["2010"],
    "month": ALL_MONTHS,
    "day": ALL_DAYS,
    "time": ALL_HOURS,
    "data_format": "grib",
    "download_format": "zip"
}

client = cdsapi.Client()
client.retrieve(ERA5_LAND, request).download()

'''generate cds api request'''

type Selection = list[str]

def generate_cds_request(
        variables: Selection, 
        year: Selection = ['2010'], 
        month: Selection = ALL_MONTHS, 
        day: Selection = ALL_DAYS, 
        time: Selection = ALL_HOURS, 
        product_type: Selection = ['reanalysis'],
        data_format: str = 'grib',
        download_format: str = 'zip') -> dict:
    '''
    Generates a <request> that can be passed into the client.retrieve(dataset, <request>) method
    Takes standard input variables and outputs a dict -- variables taken are
    - variable: set of variables used
    - year: year(s) of wanted -- should be entered as a list, even if just one year -- by default, 2010 is selected
    - month: by default, ALL_MONTHS provided (ie Jan-Dec inclusive)
    - day: by default, ALL_DAYS provided (ie 1-31 inclusive) // what happens if query for an invalid day? (eg 30th of Feb)
    - time: hour(s) wanted in form hh:mm; 24h clock -- by default, ALL_HOURS provided (0:00 to 23:00 inclusive)
    - product_type: by default, 'reanalysis' selected -- other options are related to ensemble but not particularly relevant here
    - data_format: by default, 'grib' -- NetCDF4 is just worse (i have no reason to use it)
    - download_format: by default, 'zip' -- alternative is 'unarchived' but i'm kinda concerned that'd make the download hella slow
    '''
    
    request = {"product_type": product_type,
    "variable": variables,
    "year": year,
    "month": month,
    "day": day,
    "time": time,
    "data_format": data_format,
    "download_format": download_format}

    return request
'''define standard requests'''

years_of_interest = [
    '2010', '2011', '2012', '2013', '2014'
]

input_variables = [
    '2m_dewpoint_temperature',
    '2m_temperature', 'skin_temperature',
    'daily mean precipitation',
    '10m_u_component_of_wind', '10m_v_component_of_wind',
    'total_precipitation',
    'leaf_area_index_high_vegetation','leaf_area_index_low_vegetation',
    'high_vegetation_cover', 'low_vegetation_cover',
    'type_of_high_vegetation', 'type_of_low_vegetation',
    'volumetric_soil_water_layer_1'] + ['volumetric_soil_water_layer_2',
    'volumetric_soil_water_layer_3',
    'volumetric_soil_water_layer_4',    
    'surface_pressure'
]

'''send request'''

client = cdsapi.Client()

for variable in input_variables:

    request = generate_cds_request(
        variable,
        years_of_interest
    )

    dataset = ERA5_LAND

    client.retrieve(dataset, request).download()