import sys
import os
import json
import pandas as pd
import yaml
import argparse
import joblib

params = yaml.safe_load(open('params.yaml'))#['base']

def evaluate(config_path):
    test_data_path = params["split_data"]["test_path"]
    model_dir = params["model_dir"]
    model_path = os.path.join(model_dir, "model.joblib")
    results_path = params["results"]["results_path"]

    # load features
    test_features = pd.read_csv(test_data_path, sep=",")
    X_test = test_features.iloc[:,:-1]
    y_test = test_features.iloc[:,-1]

    feature_cols=[]
    for column in X_test:
        feature_cols.append(column)
    target_col=[]
    for column in y_test:
        target_col.append(column)
        
    # load model
    with open(model_path, 'rb') as f:
        model = joblib.load(f)

    # make predictions
    predictions = model.predict(X_test)

    # generate scores
    score = model.score(X_test, y_test)
    intercept = model.intercept_[0]
    coefficients = list(zip(feature_cols, model.coef_[0]))

    # save scores
    with open(results_path, 'w') as f:
        json.dump({'score': score}, f)
        json.dump({'intercept': intercept}, f)
        json.dump({'coefficients': coefficients}, f)

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    evaluate(config_path = parsed_args.config)