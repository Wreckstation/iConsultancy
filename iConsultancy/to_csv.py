import pandas as pd

def json_to_csv(responsejson, filename='output.csv'):
    return json_to_df(responsejson).to_csv(filename)

def json_to_df(responsejson):
    try:
        json_norm = pd.json_normalize(responsejson, record_path="deals")
        return json_norm
    except TypeError:
        raise Exception("json_to_csv uses a JSON object")
