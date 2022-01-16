

from dagster import ModeDefinition, job 

from data_pipeline_complex.resources import azurite_resource, BlobStorageConnector


from data_pipeline_complex.ops import (
    container_name,
    sub_container_name,
    upload_data_to_blob,
    split_flightdata,
    filetype_parquet,
    str_number
)



local_blob_mode = ModeDefinition(
    "azurite_blob", 
    resource_defs={
        "adls": azurite_resource
    }
)


@job(resource_defs={"adls": azurite_resource})
def flight_data_to_blob():
    containername = container_name()
    subcontainername = sub_container_name()

    parquet_filetype= filetype_parquet()

    month_number=str_number()

    month_data=split_flightdata(month=month_number)

    upload_data_to_blob(data = month_data, 
        container_name=containername, 
        subcontainer=subcontainername, 
        filename=month_number, 
        filetype=parquet_filetype)














