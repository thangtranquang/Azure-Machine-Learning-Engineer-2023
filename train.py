from sklearn.linear_model import LogisticRegression
import argparse
import os
import numpy as np
from sklearn.metrics import mean_squared_error
import joblib
from sklearn.model_selection import train_test_split
import pandas as pd
from azureml.core.run import Run
from azureml.data.dataset_factory import TabularDatasetFactory

data_path= 'https://raw.githubusercontent.com/thangtranquang/Azure-Machine-Learning-Engineer-2023/main/data/heart_failure_clinical_records_dataset.csv'


#define x and y
def ds(df):
    y=df.pop('DEATH_EVENT')
    X=df
    return X,y


data= TabularDatasetFactory.from_delimited_files(path=data_path)
data= data.to_pandas_dataframe()
X,y=ds(data)


#Split data into train and test sets.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)
run = Run.get_context(allow_offline=True)



def main():
    # Add arguments to script
    parser = argparse.ArgumentParser()

    parser.add_argument("--C", type=float, default=1.0, help="Inverse of regularization strength. Smaller values cause stronger regularization")
    parser.add_argument("--max_iter", type=int, default=100, help="Maximum number of iterations to converge")

    args = parser.parse_args()

    run.log("Regularization Strength:", np.float(args.C))
    run.log("Max iterations:", np.int(args.max_iter))

    model = LogisticRegression(C=args.C, max_iter=args.max_iter).fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)
    run.log("Accuracy", np.float(accuracy))

    os.makedirs("outputs",exist_ok=True)
    joblib.dump(value=model,filename="./outputs/model.joblib")

if __name__ == '__main__':
    main()