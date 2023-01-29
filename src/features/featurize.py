import sys
import os
import yaml
import pandas as pd
import numpy as np
import pickle
from scipy.optimize import minimize
import haversine as hs
from haversine import Unit
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler, PolynomialFeatures, FunctionTransformer
from sklearn.model_selection import train_test_split
from sklearn.cross_decomposition import PLSRegression
from sklearn.decomposition import PCA
import sklearn.metrics as metrics
from sklearn.feature_extraction.text import TfidfVectorizer

# read command line params

# if len(sys.argv) != 3:
#     sys.stderr.write('Arguments error. Usage:\n')
#     sys.stderr.write(
#         '\tpython featurize.py data-dir-path features-dir-path\n'
#     )
#     sys.exit(1)

# data_path = sys.argv[1]
# features_path = sys.argv[2]

# os.makedirs(features_path, exist_ok=True)

data_path = os.makedirs("../data/prepared")

# data_input_file = os.path.join(data_path, 'train.csv')
# test_input_file  = os.path.join(data_path, 'test.csv')

# todo: do we need to import the data already seperated as train/test? Otherwise we can change this snippet
# read the data from file

data = pd.read_csv("../data/prepared/full_dataset.csv")

# todo loop which scales the numeric features
scaler = StandardScaler()

data["rssi"] = scaler.fit_transform(data["rssi"].values.reshape(-1, 1))
data["snr"] = scaler.fit_transform(data["snr"].values.reshape(-1, 1))
data["frequency"] = scaler.fit_transform(data["frequency"].values.reshape(-1, 1))
data["distance"] = scaler.fit_transform(data["distance"].values.reshape(-1, 1))
 
label = LabelEncoder()

data["datarate"] = label.fit_transform(data["datarate"])

# for i in range(len(data)):
#     data["distance"][i] = hs.haversine(
#         (data["challengee_lat"].iloc[i], data["challengee_lng"].iloc[i]),
#         (data["witness_lat"].iloc[i], data["witness_lng"].iloc[i]),
#         unit=Unit.METERS
#     )
    
def splitter(inputdata):
    #inp = inputdata.reset_index(drop=True)
    train, test = train_test_split(
        inputdata,
        test_size=0.3,
        random_state=42
    )
    train.to_csv(data_path + "/train.csv", sep=",", index=False, encoding="utf-8")
    test.to_csv(data_path + "/test.csv", sep=",", index=False, encoding="utf-8")
    
# def extract_column(column, df_path):
#     df = get_df(df_path)
#     corpus = df[[column]]

#     return corpus

# def get_train_and_test_corpus(df_1, df_2):
#     corpus_train = df_1["text"]
#     corpus_test = df_2["text"]

#     return corpus_train.append(corpus_test) 

# def append_labels_and_save_pkl(df, tfidf_matrix, filename):
#     output_file = os.path.join(features_path, filename)
#     target = df[["target"]]
#     output = pd.concat([pd.DataFrame(tfidf_matrix.toarray()), target], axis=1)

#     with open(output_file, 'wb') as f:
#         pickle.dump(output, f)   
        
# vectorizer = TfidfVectorizer()

# corpus = get_train_and_test_corpus(data_input_file, test_input_file)
# vectorizer.fit(corpus)


# train_matrix = vectorizer.transform(data_input_file["text"])
# test_matrix = vectorizer.transform(test_input_file["text"])


# append_labels_and_save_pkl(data_input_file, train_matrix, 'train.pkl')
# append_labels_and_save_pkl(test_input_file, test_matrix, 'test.pkl') 