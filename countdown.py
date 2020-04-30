#! /usr/bin/env python3

import time
from datetime import datetime
import helpers

print("Time data must be in 24 hrs format!")
end = input("Type ending time (hh:mm:ss dd-mm-yyyy) ->  ").strip()

if helpers.is_datetime(end):
    try:
        end_dt = helpers.to_datetime(end)
        now = datetime.now().strftime('%H:%M:%S %d-%m-%Y')
        now = helpers.to_datetime(now)

        try:
            while now <= end_dt:
                lacks = datetime.now().strftime('%H:%M:%S %d-%m-%Y')
                lacks = helpers.to_datetime(lacks)
                print(end_dt - lacks)
                time.sleep(1)
        except KeyboardInterrupt:
            print("Bye!")
    except ValueError:
        print("Date is not correct.")

