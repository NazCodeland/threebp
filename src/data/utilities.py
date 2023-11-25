import os

def save_df_as_csv(df, filename):
    """
    Saves a DataFrame as a CSV file.

    :param df: The DataFrame to be saved.
    :type df: DataFrame
    :param filename: The name of the CSV file.
    :type filename: str

    This function takes a DataFrame and a filename as parameters. It constructs a file path by joining the 'src\prices' directory with the filename parameter to form the name of the CSV file. It then saves the DataFrame to this file path as a CSV file. The index of the DataFrame is not included in the CSV file. The function prints the file path and a confirmation message to the console.
    """
    file_path = os.path.join("src\prices", f"{filename}.csv")
    print('file_path', file_path)

    df.to_csv(file_path, index=False)
    print("file_created, file_path", file_path)
