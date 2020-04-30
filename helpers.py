#! /usr/bin/env python3

import datetime
import re

def is_datetime(dt: str):
    datetime_regex = re.compile("((([0-1]{0,1}[0-9]|2[0-3])(:[0-5][0-9]){2})|24:00:00)\s(([0-2]{0,1}[0-9]|3[0-1])\-([0]{0,1}[1-9]|1[0-2])\-([0-9]{4,}))")
    return bool(datetime_regex.match(dt))

def to_datetime(dt: str):
    if is_datetime(dt):
        dt = dt.split()
        dt_date = [int(i) for i in dt[1].split("-")]
        dt_time = [int(j) for j in dt[0].split(":")]

        return datetime.datetime(year=dt_date[2], month=dt_date[1], day=dt_date[0], hour=dt_time[0], minute=dt_time[1], second=dt_time[2]) 
    else:
        raise ValueError("Argument format is not correct.")


