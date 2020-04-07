import pandas as pd

def json_to_csv(responsejson, filename=None):
    try:
        json_norm = pd.json_normalize(responsejson, record_path="deals")
        return json_norm.to_csv(filename)
    except TypeError:
        raise Exception("json_to_csv uses a JSON object")
