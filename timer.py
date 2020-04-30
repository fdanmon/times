#! /usr/bin/env python3

from datetime import datetime
import helpers

print("Time data must be in 24 hrs format!")
start = input("Type start time (hh:mm:ss dd-mm-yyyy) -> ").strip()
end = input("Type ending time (hh:mm:ss dd-mm-yyyy) ->  ").strip()

if helpers.is_datetime(start) and helpers.is_datetime(end):
    try:
        start_dt = helpers.to_datetime(start)
        end_dt = helpers.to_datetime(end)

        if start_dt <= end_dt:
            wait_time = end_dt - start_dt
            print(wait_time)

        else:
            raise ValueError("Start must not be lower than end.")
    except ValueError:
        print("Date is not correct.")

else:
    print("Some date is not correct.")
