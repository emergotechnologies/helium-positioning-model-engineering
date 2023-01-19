import os
import yaml
import pandas as pd

#read params

params = yaml.safe_load(open('params.yaml'))['prepare']

features = params['features'] 

# create folder to save file

data_path = os.path.join('data', 'prepared')
os.makedirs(data_path, exist_ok= True)

data = pd.read_pickle("enter_data_source in here")

data_train = data(subset = 'train', features= 'features')
data_test = data(subset = 'test', features= 'features')

def data_to_csv(split_name, data):
    df = pd.DataFrame([data.data, data.target.tolist()]).T
    df.columns = ['challengee_lat', 'challengee_lon', 'witness_lat', 'witness_lat', 'signal', 'snr', 'datarate', 'time']

    df_target_names = pd.DataFrame(data.target_names)
    df_target_names.columns = ['distance']

    out = pd.merge(df, df_target_names, left_on='target', right_index=True)
    out.to_csv(os.path.join(data_path, split_name+".csv"))
    
data_to_csv('train', data_train)   
data_to_csv('test', data_test) 
