
from dagster import repository

# from dagster import RunRequest
# from dagster import daily_schedule, sensor

from data_pipeline.jobs import data_blob_to_blob
from data_pipeline.jobs import dagster_pipeline_sensor
from data_pipeline.trigger import sensor_data_change


@repository
def data_pipeline():
    return [data_blob_to_blob]


@repository
def sensor_pipeline():
    return [dagster_pipeline_sensor, sensor_data_change]


