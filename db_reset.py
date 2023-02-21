#pip install schedule

import datetime
import schedule
import time
import sqlite3
from contextlib import closing

# データベース名
dbname = "gpt.db"

def job():
    with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()
        drop_table = "DROP TABLE IF EXISTS users"
        c.execute(drop_table)
        print("データベースをリセットしました")
        print(datetime.datetime.now())
        
schedule.every().day.at("00:00").do(job)

while True:
  schedule.run_pending()
  time.sleep(60)