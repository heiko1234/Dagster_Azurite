
import pandas as pd
import datetime as dt
from datetime import timedelta


def datetime_range(start, end, delta):
    start = dt.datetime.strptime(start, "%Y-%m-%d")
    end = dt.datetime.strptime(end, "%Y-%m-%d")

    output = [str(end.strftime(format="%Y-%m-%m %H:%M"))]
    output

    last_date = dt.datetime.strptime(output[-1], "%Y-%m-%d %H:%M")
    last_date

    while last_date >= start:
        next = last_date - timedelta(minutes = delta)
        next
        output.append(str(dt.datetime.strftime(next, "%Y-%m-%d %H:%M")))
        output
    
    return output


def convert_strdate_to_strday(strdate):
    ini_date = dt.datetime.strptime(strdate, "%Y-%m-%d %H:%M")
    datestr = str(dt.datetime.strftime(ini_date, "%Y-%m-%d"))
    return datestr



strdate = "2022-01-10 10:15"

start = "2022-01-10"

end= "2022-01-1"
delta = 1



datetime_range(start = start, end=end, delta=1)

convert_strdate_to_strday(strdate= strdate)




