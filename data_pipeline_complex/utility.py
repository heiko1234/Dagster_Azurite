
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


def remove_fileformats(any_list):
    if not isinstance(any_list, list):
        any_list = [any_list]
    if isinstance(any_list, list):
        output = [element.split(".")[0] for element in any_list]
    return output


def all_days(start_date, end_date):
    st_date = dt.datetime.strptime(start_date, "%Y-%m-%d")
    e_date = dt.datetime.strptime(end_date, "%Y-%m-%d")
    st_date=st_date.date()
    e_date=e_date.date()
    delta = e_date-st_date
    delta

    output = []

    for i in range(delta.days +1):
        day = st_date + timedelta(days=i)
        output.append(str(day))
    
    return output


def make_timegrid(start_date, end_date, timeformat, stepsize, grid="minutes"):
    st_time = dt.datetime.strptime(start_date, timeformat)
    e_time = dt.datetime.strptime(end_date, timeformat)
    delta = e_time-st_time

    output = []

    if grid == "minutes":
        for i in range(int(delta.total_seconds()/60 + int(stepsize))/int(stepsize)):
            minutes =  st_time+timedelta(seconds=i*60*stepsize)
            output.append(dt.datetime.strftime(minutes, timeformat))
    
    if grid == "days":
        for i in range(int(delta.days/int(stepsize) + 1)):
            days =  st_time+timedelta(seconds=i*60*stepsize)
            output.append(dt.datetime.strftime(days, timeformat))
    
    output = output[::-1]
    return output


def back_in_time(str_input, dateformat):
    time = dt.datetime.strptime(str_input, dateformat)-timedelta(days=12)
    str_time = str(dt.datetime.strftime(time, dateformat))

    return str_time


def get_missing_dates(list_dates, list_downloaded_dates):
    output = [element for element in list_dates if element not in list_downloaded_dates]
    return output









