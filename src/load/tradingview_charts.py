import asyncio
import webbrowser
import pandas as pd
from lightweight_charts import Chart
import io
from datetime import datetime

async def plot_chart(data, exchange):
    light_gray = '#353843'
    dark_gray = '#16161E'
    up = light_gray
    down = light_gray
    red = '#D1161E'

    # Create a new chart
    chart = Chart(title='Your Chart Title', toolbox=True, width=1000, inner_width=0.7, inner_height=1)

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
            # df['color'] = light_gray
            # df.loc[(df['Close'] > df['Close'].shift(1)) & (df['High'] > df['High'].shift(2)), 'color'] = 'green'
            chart.set(df, render_drawings=True)

    # Add a top bar with a switcher for each interval
    chart.topbar.switcher('timeframe', tuple(data.dfs.keys()), default='1d',
                        func=on_timeframe_selection)

    # Set the initial data for the chart
    if '1d' in data.dfs and data.dfs['1d'] is not None:
        df = data.dfs['1d']
        # df['color'] = light_gray
        # df.loc[(df['Close'] > df['Close'].shift(1)) & (df['High'] > df['High'].shift(2)), 'color'] = 'green'
        chart.set(df, render_drawings=True)

    async def update_clock(chart):
        while chart.is_alive:
            await asyncio.sleep(1-(datetime.now().microsecond/1_000_000))
            chart.topbar['clock'].set(datetime.now().strftime('%I:%M:%S %p'))


    def on_button_press(chart):
        new_button_value = 'On' if chart.topbar['my_button'].value == 'Off' else 'Off'
        chart.topbar['my_button'].set(new_button_value)
        print(f'Turned something {new_button_value.lower()}.')
    
    def on_row_click(row):
        row['PL'] = round(row['PL']+1, 2)
        row.background_color('PL', 'green' if row['PL'] > 0 else 'red')

        table.footer[1] = row['Ticker']
        url = "https://finance.yahoo.com/chart/" + row['Ticker'] 
        webbrowser.open(url)



    # subchart = chart.create_subchart(width=0.3, height=0.5)
    # df = data.dfs['1d']
    # subchart.set(df)

    table = chart.create_table(
        width=0.3, height=1,
        headings=('Ticker', 'Quantity', 'Status', '%', 'PL'),
        widths=(0.2, 0.1, 0.2, 0.2, 0.3),
        alignments=('center', 'center', 'right', 'right', 'right'),
        position='left', func=on_row_click)

    table.format('PL', f'£ {table.VALUE}')
    table.format('%', f'{table.VALUE} %')

    table.new_row('SPY', 3, 'Submitted', 0, 0)
    table.new_row('AMD', 1, 'Filled', 25.5, 105.24)
    table.new_row('NVDA', 2, 'Filled', -0.5, -8.24)
    table.new_row('NVDA', 2, 'Filled', -0.5, -8.24)
    table.new_row('NVDA', 2, 'Filled', -0.5, -8.24)
    table.new_row('NVDA', 2, 'Filled', -0.5, -8.24)

    def on_footer_click(table, box_index):
        print(f'Box number {box_index+1} was pressed.')

    table.footer(3, func=on_footer_click)
    table.footer[0] = 'Text Box 1'
    table.footer[1] = 'Text Box 2'
    table.footer[2] = 'Text Box 3'
      
    # Show the chart
    chart.topbar.textbox('clock')
    chart.topbar.button("my_button", "Off", func=on_button_press)

    # This line of code runs both chart.show_async(block=True) and update_clock(chart) concurrently

    # -----------------------------------------------------------------------------------------
    # multiple charts example
    
    # chart = Chart(inner_width=0.5, inner_height=0.5)
    # chart2 = chart.create_subchart(position='right', width=0.5, height=0.5)
    # chart3 = chart.create_subchart(position='left', width=0.5, height=0.5)
    # chart4 = chart.create_subchart(position='right', width=0.5, height=0.5)

    # # chart.watermark('5m')
    # # chart2.watermark('1h')
    # # chart3.watermark('Daily')
    # # chart4.watermark('4')

    # chart.set(data.dfs['5m'])
    # chart2.set(data.dfs['60m'])
    # chart3.set(data.dfs['1d'])
    # chart4.set(data.dfs['1mo'])
    
    # await chart.show_async(block=True)
    # -----------------------------------------------------------------------------------------


    
    await asyncio.gather(chart.show_async(block=True), update_clock(chart))