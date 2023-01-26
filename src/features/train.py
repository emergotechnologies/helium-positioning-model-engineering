import os
import pandas as pd
from sklearn.linear_model import LinearRegression
import yaml
import argparse
import joblib



params = yaml.safe_load(open('params.yaml'))#['base']

def train(config_path):
    #config = read_params(config_path)
    test_data_path = params["split_data"]["test_path"]
    train_data_path = params["split_data"]["train_path"]
    model_dir = params["model_dir"]
    target = [params["base"]["target_col"]]
    train = pd.read_csv(train_data_path, sep=",")
    print("Train Size", train.shape[0])
    test = pd.read_csv(test_data_path, sep=",")
    print("Test Size", test.shape[0])

    train_y = train[target]
    train_x = train.drop(target, axis=1)

    # Build linear regression model
    model = LinearRegression().fit(train_x, train_y)
    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "model.joblib")
    print("Export Joblib to ", model_path)
    joblib.dump(model, model_path)
    print("joblib exported")


if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    train(config_path = parsed_args.config)
