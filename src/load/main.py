from load.charts import plot_chart

# load/main.py
async def load(transformed_data, exchange):
    # Code to load data goes here
    print(f"Loading data: {transformed_data}")
    await plot_chart(transformed_data, exchange)
