import sys
import os
import json
import pandas as pd
import sklearn.metrics as metrics
import numpy as np
import yaml
import argparse
import joblib


params = yaml.safe_load(open('params.yaml'))#['base']

def evaluate(config_path):
    counter=1
    #declare paths
    test_data_path = params["split_data"]["test_path"]
    model_dir = params["model_dir"]
    results_path = params["results"]["results_path"]

    # load features
    test_features = pd.read_csv(test_data_path, sep=",")
    X_test = test_features.iloc[:,:-1]
    y_test = test_features.iloc[:,-1]
    with open(results_path, 'w') as f:
        for root, dirs, files in os.walk("models"):
            for file in files:
                if file.endswith(".joblib"):
                    model_path = os.path.join(model_dir, f"{file}")

                    feature_cols=[]
                    for column in X_test:
                        feature_cols.append(column)
                    target_col=[]
                    for column in y_test:
                        target_col.append(column)
                        
                    # load model
                    with open(model_path, 'rb') as model_load:
                        model = joblib.load(model_load)

                    # make predictions
                    y_pred = model.predict(X_test)

                    # generate scores
                    # Regression metrics
                    explained_variance=metrics.explained_variance_score(y_test, y_pred)
                    mean_absolute_error=metrics.mean_absolute_error(y_test, y_pred) 
                    mse=metrics.mean_squared_error(y_test, y_pred) 
                    median_absolute_error=metrics.median_absolute_error(y_test, y_pred)
                    r2=metrics.r2_score(y_test, y_pred)
                    score = model.score(X_test, y_test)
                    #coefficients = list(zip(feature_cols, model.coef_[0]))

                    # save scores
                    json.dump({\
                        f'model{counter}': {'model_name':f'{file}', 'score': score, \
                        'explained_variance': round(explained_variance,4),'r2': round(r2,4),\
                        'MeanAE': round(mean_absolute_error,4), 'MedianAE': round(median_absolute_error,4),\
                        'MSE': round(mse,4), 'RMSE': round(np.sqrt(mse),4)}\
                        },  f, indent = 2)

                    # json.dump({f'model{counter}': f'{file}'}, f, indent = 2)
                    # json.dump({'score': score}, f)
                    # #json.dump({'coefficients': coefficients}, f)
                    # json.dump({'explained_variance': round(explained_variance,4)}, f)   
                    # json.dump({'r2': round(r2,4)}, f)
                    # json.dump({'MeanAE': round(mean_absolute_error,4)}, f)
                    # json.dump({'MedianAE': round(median_absolute_error,4)}, f)
                    # json.dump({'MSE': round(mse,4)}, f)
                    # json.dump({'RMSE': round(np.sqrt(mse),4)}, f)
                    # json.dump('\n', f)

                    # with open(results_path, 'w') as f:
                    #     f.write(f'model{counter}: {file}\n')
                    #     f.write(f'score: {score}\n')
                    #     f.write(f'explained_variance: {round(explained_variance,4)}\n')   
                    #     f.write(f'r2: {round(r2,4)}\n')
                    #     f.write(f'MeanAE: {round(mean_absolute_error,4)}\n')
                    #     f.write(f'MedianAE: {round(median_absolute_error,4)}\n')
                    #     f.write(f'MSE: {round(mse,4)}\n')
                    #     f.write(f'RMSE: {round(np.sqrt(mse),4)}\n\n')
                    
                    
                    counter+=1

if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    evaluate(config_path = parsed_args.config)