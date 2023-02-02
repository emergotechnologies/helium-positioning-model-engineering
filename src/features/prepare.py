import os
import yaml
import pandas as pd
from sklearn.model_selection import train_test_split
import haversine as hs
from haversine import Unit
import shutil
import click
# read params

#params = yaml.safe_load(open('params.yaml'))['prepare']

#features = params['features'] 

# create folder to save file

data_path = os.path.join('data', 'prepared')
os.makedirs(data_path, exist_ok= True)

#flag="google_sheets"
@click.command()
@click.option('--file_origin', default="google_sheets", type=str, help='where the data is loaded from: google_sheets or helium_wrapper')

def prepare_data(file_origin):
    if file_origin == "helium":
        data = pd.read_pickle("./data/raw/remote_storage/challenges.pkl")
        data = data.reset_index(drop=True)
        #data = data[["witness_lat","witness_lng","signal","distance"]]
        data = data.rename(columns={"signal":"rssi"})

    if file_origin == "google_sheets":
        file_list=[]
        for root,dirs,files in os.walk("data/raw/experiments"):
            for file in files:
                file_path = root+"/"+file
                print(file_path)
                file_list.append(file_path)
        
        assert len(file_list) > 0 ,"no files found"

        data = pd.concat(map(pd.read_csv, file_list), ignore_index=True)
        data = data.rename(columns={"hotspot_lat":"witness_lat", "hotspot_long":"witness_lng", "node_lat":"challengee_lat", "node_lng":"challengee_lng", \
        "hotspot_rssi":"rssi", "hotspot_snr":"snr", "hotspot_spreading": "datarate", "hotspot_frequency": "frequency"})

        distance=[]
        for i in range(len(data)):
            distance.append(hs.haversine(
                (data["challengee_lat"].iloc[i], data["challengee_lng"].iloc[i]),
                (data["witness_lat"].iloc[i], data["witness_lng"].iloc[i]),
                unit=Unit.METERS
            ))
        data["distance"]=distance
        file_destination = "data/raw/remote_storage"
        for file_origin in file_list:
            shutil.copy2(file_origin, file_destination)

    data = data[["rssi","snr","datarate","frequency","distance"]]
    #data = data[["rssi","snr","datarate","distance"]]

    data.to_csv(data_path + "/full_dataset.csv", sep=",", index=False, encoding="utf-8")

prepare_data()


