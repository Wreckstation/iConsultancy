import pandas as pd

def json_to_csv(responsejson):
    try:
        json_norm = pd.json_normalize(responsejson, record_path="deals")
        return json_norm.to_csv()
    except TypeError:
        raise Exception("json_to_csv uses a JSON object")
