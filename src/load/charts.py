import pandas as pd
from lightweight_charts import Chart
import io

def plot_chart(data):
    chart = Chart()
    chart.set(data)
    chart.show(block=True)

if __name__ == '__main__':
    
    # Read the CSV file
    df = pd.read_csv('src/prices/symbols/CCO.TO.csv')
    # Reverse the order of the DataFrame rows
    print(df.head())
    df = df.iloc[::-1]
    print(df.head())
    plot_chart(df)
