

from dagster import ModeDefinition, job 

from data_pipeline.mock_azurite import azurite_resource
from data_pipeline.ops import local_name_string, blob_name_string
from data_pipeline.ops import container_name, blob_where_to_safe
from data_pipeline.ops import load_csv_from_blob, upload_data_to_blob
from data_pipeline.ops import call_local_data
from data_pipeline.ops import sensor_op, local_dump_data



local_blob_mode = ModeDefinition(
    "azurite_blob",
    resource_defs={
        "adls": azurite_resource,
    },
)


@job(resource_defs={"adls": azurite_resource})
def data_blob_to_blob():

    namestring = blob_name_string()
    containername = container_name()
    wheretosafe = blob_where_to_safe()

    loaded_data = load_csv_from_blob(
        container_name=containername,
        filename=namestring
    )


    # loaded_data = call_local_data(path = namestring)


    upload_data_to_blob(
        df = loaded_data,
        container_name=containername,
        filename=wheretosafe
    )


@job()
def dagster_pipeline_sensor():

    namestring = local_name_string()

    loaded_data = call_local_data(path = namestring)

    df = sensor_op(loaded_data)

    local_dump_data(data=df, path= namestring)

