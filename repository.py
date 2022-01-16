
from dagster import repository

# from dagster import RunRequest
# from dagster import daily_schedule, sensor

from data_pipeline.jobs import data_blob_to_blob
from data_pipeline.jobs import dagster_pipeline_sensor
from data_pipeline.trigger import sensor_data_change

from data_pipeline_complex.jobs import flight_data_to_blob
from data_pipeline_complex.trigger import sensor_flight_data

@repository
def data_pipeline():
    return [data_blob_to_blob]


@repository
def sensor_pipeline():
    return [
        dagster_pipeline_sensor, 
        sensor_data_change, 
        flight_data_to_blob, 
        sensor_flight_data
        ]



