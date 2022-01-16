

import datetime as dt

from data_pipeline_complex.jobs import flight_data_to_blob

from data_pipeline_complex.resources import (
    # AzuriteResource,
    BlobStorageConnector,
    # get_container_client
)

from data_pipeline_complex.utility import (
    back_in_time
)

from data_pipeline_complex.utility import all_days, remove_fileformats, get_missing_dates

from dagster import get_dagster_logger, RunRequest, sensor, schedule





@sensor(job= flight_data_to_blob, minimum_interval_seconds=60)
def sensor_flight_data(context):

    last_mod_time = str(context.cursor) if context.cursor else 0
    containername = "azuriteblob"
    subcontainername = "flights"
    filetype_parquet = "parquet"
    
    end_date = str(dt.datetime.now().date())


    list_downloaded_files = BlobStorageConnector(container_name="azuriteblob").list_files_in_subcontainer(subcontainer=subcontainername, file = filetype_parquet)
    
    #list_downloaded_files

    start_date = back_in_time(str_input=end_date, dateformat = "%Y-%M-%d")
    list_of_dates = all_days(start_date = start_date, end_date = end_date)

    list_blobs = remove_fileformats(any_list=list_downloaded_files)

    missing_dates = get_missing_dates(list_of_dates, list_blobs)


    last_file = missing_dates[-1]
    last_file

    number_of_files = str(len(list_blobs))

    if last_file is None:
        return False
    
    #if last_file == last_mod_time:
    #    return False
    
    if last_file is not None:
        
        yield RunRequest(
            run_key = f"updated_runkey_{number_of_files}",
            run_config={
                "ops":{
                    "str_number":{
                        "config": {
                            "number_month": number_of_files
                        }
                    }
                }
            }
        )

        context.update_cursor(str(last_file))




