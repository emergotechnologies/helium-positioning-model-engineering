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
from sklearn.cross_decomposition import PLSRegression
from sklearn.decomposition import PCA
import sklearn.metrics as metrics
from sklearn.feature_extraction.text import TfidfVectorizer

# read command line params
if len(sys.argv) != 3:
    sys.stderr.write('Arguments error. Usage:\n')
    sys.stderr.write(
        '\tpython featurize.py data-dir-path features-dir-path\n'
    )
    sys.exit(1)

data_path = sys.argv[1]
features_path = sys.argv[2]

os.makedirs(features_path, exist_ok=True)

#todo add filename
data_input_file = os.path.join(data_path, 'input.csv')
test_input_file  = os.path.join(data_path, 'test.csv')

# todo: do we need to import the data already seperated as train/test? Otherwise we can change this snippet
# read the data from file
data = pd.read_csv(data_input_file)

label = LabelEncoder()

data["datarate"] = label.fit_transform(data["datarate"])

for i in range(len(data)):
    data["distance"][i] = hs.haversine(
        (data["challengee_lat"].iloc[i], data["challengee_lng"].iloc[i]),
        (data["witness_lat"].iloc[i], data["witness_lng"].iloc[i]),
        unit=Unit.METERS
    )
    