from apscheduler.schedulers.background import BackgroundScheduler
from database import download_data, upload_to_db

def job(symbol, timeframe):
    try:
        data = download_data(symbol, timeframe)
        upload_to_db(data, symbol, timeframe)
    except Exception as e:
        print(f"An error occurred while running job for {symbol} {timeframe}: {e}")

scheduler = BackgroundScheduler()

def schedule_tasks(symbol, timeframe):
    if timeframe == '1Min':
        # Schedule a task to run every 1 minute from Monday to Friday, starting at 9:30:01 AM
        scheduler.add_job(job, 'cron', day_of_week='mon-fri', hour='9-17', minute='*/1', second=1, args=[symbol, timeframe])
        print(f"Scheduled {symbol} 1Min Task")
    elif timeframe == '5Min':
        # Schedule a task to run every 5 minutes from Monday to Friday, starting at 9:30:01 AM
        scheduler.add_job(job, 'cron', day_of_week='mon-fri', hour='9-17', minute='*/5', second=1, args=[symbol, timeframe])
        print(f"Scheduled {symbol} 5Min Task")
    elif timeframe == '1h':
        # Schedule a task to run every hour from Monday to Friday, starting at 9:31 AM
        scheduler.add_job(job, 'cron', day_of_week='mon-fri', hour='9-17', minute=31, args=[symbol, timeframe])
        print(f"Scheduled {symbol} Hourly Task")
    elif timeframe == 'd':
        # Schedule a task to run every day at 9:30 AM from Monday to Friday
        scheduler.add_job(job, 'cron', day_of_week='mon-fri', hour=9, minute=30, args=[symbol, timeframe])
        print(f"Scheduled {symbol} Daily Task")
    elif timeframe == 'wk':
        # Schedule a task to run at 9 PM every Friday
        scheduler.add_job(job, 'cron', day_of_week='fri', hour=21, args=[symbol, timeframe])
        print(f"Scheduled {symbol} Weekly Task")
    elif timeframe == 'mo':
        # Schedule a task to run on the last day of every month at 9 PM
        scheduler.add_job(job, 'cron', day='last', hour=21, args=[symbol, timeframe])
        print(f"Scheduled {symbol} Monthly Task")

    if not scheduler.running:
        scheduler.start()
