import json
import os
import pickle

def save_dataframe(data:str, filename: str) -> None:
    """
    Saves a DataFrame as a local file.

    :param data: The data to be saved. Can be a DataFrame or a dictionary of DataFrames.
    :type data: DataFrame or dict
    :param filename: The name of the file.
    :type filename: str
    """

    file_path = os.path.join("src/prices", f"{filename}.json")
    with open(file_path, 'w') as f:
        json.dump(data, f)

    print("json file_created:", file_path)

def save_pickle_object(obj, filename):
    path = 'src/prices/'  # Hardcoded path
    filename = f"{filename}.pkl"
    with open(os.path.join(path, filename), 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)
    
    print('pickle object saved')

def load_pickle_object(filename):
    path = 'src/prices/'  # Hardcoded path
    filename = f"{filename}.pkl"
    with open(os.path.join(path, filename), 'rb') as f:
        return pickle.load(f)
