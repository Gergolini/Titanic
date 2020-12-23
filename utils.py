import pandas as pd

def update_submission(X_test, model, fpath, target):
    y_pred = model.predict(X_test)
    df = pd.read_csv(fpath)
    df[target] = y_pred
    df.to_csv(fpath, index=False)

