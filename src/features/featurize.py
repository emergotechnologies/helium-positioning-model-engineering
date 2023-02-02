import sys
import os
import yaml
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler, PolynomialFeatures, FunctionTransformer
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OrdinalEncoder
from sklearn.pipeline import Pipeline
import joblib
from sklearn.cross_decomposition import PLSRegression
from sklearn.decomposition import PCA
import sklearn.metrics as metrics
from sklearn.feature_extraction.text import TfidfVectorizer

os.makedirs("data/prepared", exist_ok=True)

data_path = "data/prepared"

# for testing purposes only 
data = pd.read_csv("../data/prepared/full_dataset.csv")

numeric_features = ["snr", "rssi", "frequency", "distance"]

numeric_transformer = Pipeline(steps=[("scaler", StandardScaler())])

categorical_features = ["datarate"]

categorical_transformer = Pipeline(steps=[("encoder", OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value= -1)),])

preprocessor = ColumnTransformer(transformers=[("num", numeric_transformer, numeric_features),("cat", categorical_transformer, categorical_features),])

# save preprocessor as joblib
joblib.dump(preprocessor, "preprocess.joblib")


def splitter(inputdata):
    #inp = inputdata.reset_index(drop=True)
    train, test = train_test_split(
        inputdata,
        test_size=0.3,
        random_state=42
    )
    train.to_csv(data_path + "/train.csv", sep=",", index=False, encoding="utf-8")
    test.to_csv(data_path + "/test.csv", sep=",", index=False, encoding="utf-8")
    
splitter(data)

append_labels_and_save_pkl(data_input_file, train_matrix, 'train.pkl')
append_labels_and_save_pkl(test_input_file, test_matrix, 'test.pkl') 
