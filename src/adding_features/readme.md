# Adding Features

The features added are sea_height and artificial_brightness.
They are implemented on the dataset (improved_dataset.pkl) in this folder.
Due to time shortage they were not yet implemented for google sheets data in a pipeline and .

In this folder is one Notebook, one modul which gets imported into the Notebook and one improved dataset on the dataset we accumulated in November with about 1500 datainputs.

The modul consists of two functions, the first function has the input longitude and latitude and gets the seaheight through an api (https://api.open-meteo.com). The second function has the following inputs: longitude, latitude, layer and type. Longitude and Latitude are needed from the desired location. Additionally the layer is the type of lightmap needed. There are various types but mostly its just from the recent years, e.g.: "viirs_2013" to "viirs_2021" and "wa_2015", which are two different types of acquiring the artificial brightness levels and the creators of the lightmap website decided to continue only with the VIIRS variation. This data is also acquired through an api of the website https://www.lightpollutionmap.info. I contacted one of the creators of the API Jurij Stare and he gave me permission to use this API-key for the Project, since Lightmap-API is not usable without an API-key. This API-key is in the files, but is not for public use!

The Notebook exists of only one function with with 4 inputs: lat, long, input_path_pickle_file, ouput_path_pickle_file.
The lat, long of the desired location. The input pickle file which should be updated and the output name of the updated pickle file.