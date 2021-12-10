
from dagster import repository

# from dagster import RunRequest
# from dagster import daily_schedule, sensor

from data_pipeline.jobs import data_blob_to_blob



@repository
def data_pipeline():
    return [data_blob_to_blob]




