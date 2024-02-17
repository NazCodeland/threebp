import json
import os
import pickle
import pandas as pd
import webbrowser
import datetime


def save_dataframe(data:str, filename: str) -> None:
    """
    Saves a DataFrame as a local file.

    :param data: The data to be saved. Can be a DataFrame or a dictionary of DataFrames.
    :type data: DataFrame or dict
    :param filename: The name of the file.
    :type filename: str
    """

    file_path = os.path.join("src\prices", f"{filename}.json")
    with open(file_path, 'w') as f:
        json.dump(data, f)
    print("json file_created:", file_path)

def save_pickle_object(obj, filename):
    path = 'src\prices'  # Hardcoded path
    filename = f"{filename}.pkl"
    with open(os.path.join(path, filename), 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
    
    print('pickle object saved')

def load_pickle_object(filename):
    path = 'src\prices'  # Hardcoded path
    filename = f"{filename}.pkl"
    with open(os.path.join(path, filename), 'rb') as f:
        return pickle.load(f)

def get_file_as_df(file_src) -> pd.DataFrame:
    with open(file_src, 'r') as f:
        f = json.load(f)
        f = pd.DataFrame(f)
        return f

def save_to_html_and_open(df):
    # Get the current date and time
    now = datetime.datetime.now()
    
    # Format it as a string with milliseconds and microseconds
    timestamp = now.strftime("%Y%m%d%H%M%S%f")
    
    # Use the timestamp to create a unique filename
    filename = f"data_{timestamp}.html"

    with open(filename, "w") as f:
        f.write(df.to_html(escape=False))
    
    webbrowser.open('file://' + os.path.realpath(filename))

