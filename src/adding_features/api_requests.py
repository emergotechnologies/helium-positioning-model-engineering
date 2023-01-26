#%%
import requests


def get_seahight(latitude_seaheight, longitude_seaheight):
    """
    query_latitude: type=str, latitude in dec e.g. 43.65 (between -90 <= x < 90)
    query_longitude: type=str, longitude in dec e.g. 94.32 (between -180 <= x < 180)
    """
    assert -90 <= latitude_seaheight < 90, "latitude must be between -90 <= latitude < 90"
    assert -180 <= longitude_seaheight < 180, "longitude must be between -180 =< longitude < 180"
    r = requests.get(f"https://api.open-meteo.com/v1/elevation?latitude={latitude_seaheight}&longitude={longitude_seaheight}")
    seaheight=r.json()['elevation'][0]
    return(seaheight)



def get_artificial_brightness(query_latitude, query_longitude, query_layer="viirs_2021", query_type="point", api_key="f7Pot9fJp6K5onYg"):
    """

    DO NOT SHARE API-KEY !!!
    
    query_latitude: type=str, latitude in dec e.g. 43.65 (between -90 <= x < 90)
    query_longitude: type=str, longitude in dec e.g. 94.32 (between -180 <= x < 180)
    query_layer: type=str, "viirs_2013","viirs_2014","viirs_2015","viirs_2016","viirs_2017","viirs_2018","viirs_2019","viirs_2020","viirs_2021","wa_2015"
    query_type: type=str, "point", "point_t" (VIIRS only), "area", "area_t" (VIIRS only). Values "point_t" or "area_t" (VIIRS only)
    """
    assert -90 <= query_latitude < 90, "latitude must be between -90 <= latitude < 90"
    assert -180 <= query_longitude < 180, "longitude must be between -180 =< longitude < 180"

    r = requests.get(f"https://www.lightpollutionmap.info/QueryRaster/?\
ql={query_layer}\
&qt={query_type}\
&qd={query_longitude},{query_latitude}\
&key={api_key}")
    artificial_brightness=r.text

    if artificial_brightness == "":
        artificial_brightness="0"
    return(float(artificial_brightness))

