import pandas as pd
from lightweight_charts import Chart
import io

async def plot_chart(data, exchange):
    light_gray = '#353843'
    dark_gray = '#16161E'
    up = light_gray
    down = light_gray
    red = '#D1161E'

    # Create a new chart
    chart = Chart(title='Your Chart Title', toolbox=True)
    
    chart.time_scale(
        right_offset= 0, 
        min_bar_spacing= 0.5,
        visible= True, 
        time_visible= True, 
        seconds_visible= False,
        border_visible= True, 
        border_color=up
    )
    
    chart.layout(
        background_color='#090008',
        text_color=light_gray,
        font_size=16, 
        font_family='Helvetica'
        )

    chart.grid(
        vert_enabled = False,
        horz_enabled = False,
        # color = UP,
        # style = 'solid'
    )

    chart.crosshair(
        mode= 'normal', 
        vert_visible = True,
        vert_width = 1, 
        vert_color = dark_gray, 
        vert_style = 'solid',
        vert_label_background_color = dark_gray, 

        horz_visible = True,
        horz_width = 1, 
        horz_color = dark_gray, 
        horz_style = 'solid',
        horz_label_background_color = dark_gray
        )

    chart.watermark(

        text='', 
        font_size= 44, 
        color= 'rgba(180, 180, 200, 0.5)'
    )

    # top left: open, high, low, close, volume
    chart.legend(
        visible = True,
        text=f'Symbol: {data.symbol} | Industry: {data.industry} | Sector: {data.sector}',
        ohlc = True, 
        percent = True, 
        lines = True,
        # color = , 
        font_size = 16, 
        font_family = 'Monaco',
        )


    chart.price_scale(
        mode= 'normal',
        align_labels = True,
        border_visible = True,
        border_color = dark_gray,
        text_color = light_gray,
        entire_text_only = False,
        ticks_visible = False,
        scale_margin_top = 0.2,
        scale_margin_bottom = 0.2
        )

    chart.candle_style(
        up_color=up, 
        down_color=down, 
        border_enabled= False,
        # color= "rgb(0, 120, 255)",
        # border_up_color= up,
        # wick_up_color= up,
        # border_down_color= down,
        # wick_down_color= down,
        # line_width= 2,
        )

    chart.volume_config(
        up_color=dark_gray, 
        down_color=dark_gray,
        scale_margin_top= 0.8, 
        scale_margin_bottom= 0.0
        )

    async def on_search(chart, string):
        print(f'Search Text: "{string}" | Chart/SubChart ID: "{chart.id}"')
        # Assuming 'exchange' is an instance of your Exchange class
        equity = exchange.get_equity_by_symbol(string)
        print("equity", equity)
        if equity is not None:
            await plot_chart(equity, exchange)
        else:
            print(f"No equity found with symbol {string}")

    chart.events.search += on_search


    # Create a function to handle timeframe selection
    def on_timeframe_selection(chart):
        selected_interval = chart.topbar['timeframe'].value
        if selected_interval in data.dfs and data.dfs[selected_interval] is not None:
            df = data.dfs[selected_interval]
            df['color'] = light_gray
            df.loc[(df['Close'] > df['Close'].shift(1)) & (df['High'] > df['High'].shift(2)), 'color'] = 'green'
            chart.set(df, render_drawings=True)

    # Add a top bar with a switcher for each interval
    chart.topbar.switcher('timeframe', tuple(data.dfs.keys()), default='1d',
                        func=on_timeframe_selection)

    # Set the initial data for the chart
    if '1d' in data.dfs and data.dfs['1d'] is not None:
        df = data.dfs['1d']
        df['color'] = light_gray
        df.loc[(df['Close'] > df['Close'].shift(1)) & (df['High'] > df['High'].shift(2)), 'color'] = 'green'
        chart.set(df, render_drawings=True)

    # Show the chart
    await chart.show_async(block=True)
