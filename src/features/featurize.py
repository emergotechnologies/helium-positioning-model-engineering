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

# for testing purposes only 
data = pd.read_csv("../data/prepared/full_dataset.csv")

numeric_features = ["snr", "rssi", "frequency", "distance"]

numeric_transformer = Pipeline(steps=[("scaler", StandardScaler())])

categorical_features = ["datarate"]

categorical_transformer = Pipeline(steps=[("encoder", OrdinalEncoder(handle_unknown="use_encoded_value", unknown_value= -1)),])

preprocessor = ColumnTransformer(transformers=[("num", numeric_transformer, numeric_features),("cat", categorical_transformer, categorical_features),])

# save preprocessor as joblib
joblib.dump(preprocessor, "preprocess.joblib")


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