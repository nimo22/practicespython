import json
import time

import requests
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.schedulers.background import  BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

import os
base="http://127.0.0.1:5000/"

response=requests.get(base)
print(response)
#js=json.loads(response)
js=response.json()

print(js['data']['local'])
"""
     text=response.iter_line()
     print(text)
     """

def job():
     print('ooki')

if __name__ == "__main__":
     scheduler = BackgroundScheduler()
     scheduler.configure(timezone="America/New_York")
     scheduler.add_job(job, 'interval', seconds=1)
     scheduler.start()

     time.sleep(2.4)



