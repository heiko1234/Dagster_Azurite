

import datetime as dt

from data_pipeline_complex.resources import AzuriteResource
from data_pipeline_complex.resources import BlobStorageConnector
from data_pipeline_complex.resources import get_container_client

from data_pipeline_complex.utility import all_days, remove_fileformats, get_missing_dates


from dagster import get_dagster_logger, RunRequest, sensor, schedule





@sensor(job= data_blob_to_blob, minimum_interval_seconds=60)
def sensor_blob_data(context):

    last_mod_time = str(context.cursor) if context.cursor else 0

    list_downloaded_files = BlobStorageConnector(container_name="azuriteblob").list_files_in_subcontainer(subcontainer="targetfolder", file = ".csv")
    #list_downloaded_files
    start_date = "2021-12-24"
    list_of_dates = all_days(start_date = start_date, end_date = str(dt.datetime.now().date()))
    #list_of_dates
    list_blobs = remove_fileformats(any_list=list_downloaded_files)
    #list_blobs
    missing_dates = get_missing_dates(list_of_dates, list_blobs)
    missing_dates

    last_file = missing_dates[-1]
    last_file

    if last_file is None:
        return False
    
    if last_file == last_mod_time:
        return False
    
    if last_file is not None:
        
        yield RunRequest(
            run_key = f"updated_runkey_{last_file}",
            run_config={
                "ops":{
                }
            }
        )

        context.update_cursor(str(last_file))




