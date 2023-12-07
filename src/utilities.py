import os
import pandas as pd

def save_df(data, filename, file_format):
    """
    Saves a DataFrame or a dictionary of DataFrames as a file in the specified format.

    :param data: The data to be saved. Can be a DataFrame or a dictionary of DataFrames.
    :type data: DataFrame or dict
    :param filename: The name of the file.
    :type filename: str
    :param file_format: The format of the file (e.g., 'csv', 'json').
    :type file_format: str
    """
    file_path = os.path.join("src\prices", f"{filename}.{file_format}")
    print('file_path', file_path)

    if file_format == 'csv':
        data.to_csv(file_path, index=False)
    elif file_format == 'json':
        data.to_json(file_path, orient='records')
    # Add more formats here as needed

        print("file_created, file_path", file_path)
    # if isinstance(data, dict):
    #     for key, df in data.items():
    #         file_path = os.path.join("src\prices", f"{filename}_{key}.{file_format}")
    #         print('file_path', file_path)

    #         if file_format == 'csv':
    #             df.to_csv(file_path, index=False)
    #         elif file_format == 'json':
    #             df.to_json(file_path, orient='records')
    #         # Add more formats here as needed

    #         print("file_created, file_path", file_path)
    # else:
    #     file_path = os.path.join("src\prices", f"{filename}.{file_format}")
    #     print('file_path', file_path)

    #     if file_format == 'csv':
    #         data.to_csv(file_path, index=False)
    #     elif file_format == 'json':
    #         data.to_json(file_path, orient='records')
    #     # Add more formats here as needed

    #     print("file_created, file_path", file_path)

def dict_to_dataframe(data, columns):
    """
    Converts a dictionary into a pandas DataFrame.

    :param data: The dictionary to be converted.
    :type data: dict
    :param columns: The list of column names for the DataFrame.
    :type columns: list
    :return: The resulting DataFrame.
    :rtype: pandas.DataFrame
    """
    df = pd.DataFrame(list(data.items()), columns=columns)
    return df

def flatten_dict(data):
    flattened_data = []

    for key, values in data.items():
        # Check if the values are a list
        if isinstance(values, list):
            # If the values are a list, iterate over the list
            for value in values:
                # For each dictionary in the list, create a new dictionary
                # that includes the key from the outer dictionary and the
                # key-value pairs from the inner dictionary
                new_dict = {'key': key, **value}
                # if all(isinstance(value, (int, float, str)) for value in new_dict.values()):
                #     df = pd.DataFrame(new_dict, index=[0])
                # else:
                #     df = pd.DataFrame(new_dict)
                # print("-----------------------------------")
                # # print(df)
                # print("-----------------------------------")

                # Append the new dictionary to the flattened_data list
                flattened_data.append(new_dict)
        else:
            # If the values are not a list
            # create a new dictionary with 'key' and 'name' keys
            new_dict = {'Symbol': key, 'name': values}
            # Append the new dictionary to the flattened_data list
            flattened_data.append(new_dict)

    return flattened_data

def flatten_nested_dict(df):
    # Convert the DataFrame to a list of dictionaries
    data_list = df.to_dict('records')

    # Initialize an empty dictionary to store the nested data
    nested_data = {}

    # Iterate over the list of dictionaries
    for data_dict in data_list:
        print(data_dict)
        key = data_dict.pop('key')

        # If the key is not in the nested_data dictionary, add it
        if key not in nested_data:
            nested_data[key] = []

        # Append the data_dict to the list of dictionaries for this key
        nested_data[key].append(data_dict)

    return nested_data

import pandas as pd
from io import StringIO

def csv_string_to_dataframe(csv_string):
    """
    Converts a CSV string to a pandas DataFrame.

    :param csv_string: The CSV string.
    :type csv_string: str

    This function takes a CSV string as a parameter. It reads the CSV string and returns a pandas DataFrame.
    """
    data = StringIO(csv_string)
    df = pd.read_csv(data)
    return df
