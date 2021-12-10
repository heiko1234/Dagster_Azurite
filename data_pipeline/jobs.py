

from dagster import ModeDefinition, job 

from data_pipeline.mock_azurite import azurite_resource
from data_pipeline.ops import name_sting, container_name, where_to_safe
from data_pipeline.ops import load_csv_from_blob, upload_data_to_blob



local_blob_mode = ModeDefinition(
    "azurite_blob",
    resource_defs={
        "adls": azurite_resource,
    },
)


@job(resource_defs={"adls": azurite_resource})
def data_blob_to_blob():

    namestring = name_sting()
    containername = container_name()
    wheretosafe = where_to_safe()

    loaded_data = load_csv_from_blob(
        container_name=containername,
        filename=namestring
    )

    upload_data_to_blob(
        df = loaded_data,
        container_name=containername,
        filename=wheretosafe
    )




