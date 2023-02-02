import sys
import os
import yaml
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler, PolynomialFeatures, FunctionTransformer
from sklearn.model_selection import train_test_split
<<<<<<< src/features/featurize.py
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OrdinalEncoder
from sklearn.pipeline import Pipeline
import joblib
=======
from sklearn.cross_decomposition import PLSRegression
from sklearn.decomposition import PCA
import sklearn.metrics as metrics
from sklearn.feature_extraction.text import TfidfVectorizer
>>>>>>> src/features/featurize.py

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

<<<<<<< src/features/featurize.py
data_path = os.makedirs("../data/prepared")

=======
os.makedirs("data/prepared", exist_ok=True)

data_path = "data/prepared"

>>>>>>> src/features/featurize.py
# data_input_file = os.path.join(data_path, 'train.csv')
# test_input_file  = os.path.join(data_path, 'test.csv')

# todo: do we need to import the data already seperated as train/test? Otherwise we can change this snippet
# read the data from file

<<<<<<< src/features/featurize.py
# for testing purposes only 
data = pd.read_csv("../data/prepared/full_dataset.csv")

numeric_features = ["snr", "rssi", "frequency", "distance"]

numeric_transformer = Pipeline(steps=[("scaler", StandardScaler())])
=======
data = pd.read_csv("data/prepared/full_dataset.csv")

# todo loop which scales the numeric features
scaler = StandardScaler()

data["rssi"] = scaler.fit_transform(data["rssi"].values.reshape(-1, 1))
data["snr"] = scaler.fit_transform(data["snr"].values.reshape(-1, 1))
data["frequency"] = scaler.fit_transform(data["frequency"].values.reshape(-1, 1))
data["distance"] = scaler.fit_transform(data["distance"].values.reshape(-1, 1))
 
label = LabelEncoder()
>>>>>>> src/features/featurize.py

categorical_features = ["datarate"]

<<<<<<< src/features/featurize.py
categorical_transformer = Pipeline(steps=[("encoder", OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value= -1)),])

preprocessor = ColumnTransformer(transformers=[("num", numeric_transformer, numeric_features),("cat", categorical_transformer, categorical_features),])

# save preprocessor as joblib
joblib.dump(preprocessor, "preprocess.joblib")


=======
>>>>>>> src/features/featurize.py
# for i in range(len(data)):
#     data["distance"][i] = hs.haversine(
#         (data["challengee_lat"].iloc[i], data["challengee_lng"].iloc[i]),
#         (data["witness_lat"].iloc[i], data["witness_lng"].iloc[i]),
#         unit=Unit.METERS
#     )
<<<<<<< src/features/featurize.py
    
=======

>>>>>>> src/features/featurize.py
def splitter(inputdata):
    #inp = inputdata.reset_index(drop=True)
    train, test = train_test_split(
        inputdata,
        test_size=0.3,
        random_state=42
    )
    train.to_csv(data_path + "/train.csv", sep=",", index=False, encoding="utf-8")
    test.to_csv(data_path + "/test.csv", sep=",", index=False, encoding="utf-8")
    
<<<<<<< src/features/featurize.py
# def extract_column(column, df_path):
#     df = get_df(df_path)
#     corpus = df[[column]]

=======

splitter(data)


# def extract_column(column, df_path):
#     df = get_df(df_path)
#     corpus = df[[column]]

>>>>>>> src/features/featurize.py
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
<<<<<<< src/features/featurize.py
# append_labels_and_save_pkl(test_input_file, test_matrix, 'test.pkl') 
=======
# append_labels_and_save_pkl(test_input_file, test_matrix, 'test.pkl') 
>>>>>>> src/features/featurize.py