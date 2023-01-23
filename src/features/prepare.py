import os
import yaml
import pandas as pd
from sklearn.model_selection import train_test_split
# read params

#params = yaml.safe_load(open('params.yaml'))['prepare']

#features = params['features'] 

# create folder to save file

data_path = os.path.join('data', 'prepared')
os.makedirs(data_path, exist_ok= True) 


#TODO  hier sollte eine Methode entstehen, um alle oder bestimmte relevante Ordner zu lesen 
# und Daten aus Experimente und/oder remote/storage und/oder Wrapper zu fetchen
data = pd.read_pickle("./data/raw/remote_storage/challenges_2.pkl")

#data_train = data_path(subset = 'train', features= 'features')
#data_test = data_path(subset = 'test', features= 'features')

def splitter(inputdata):
    train, test = train_test_split(
        data,
        test_size=0.3,
        random_state=42
    )
    train.to_csv(data_path + "/train.csv", sep=",", index=False, encoding="utf-8")
    test.to_csv(data_path + "/test.csv", sep=",", index=False, encoding="utf-8")

if __name__ =="__main__":
    splitter(data)
