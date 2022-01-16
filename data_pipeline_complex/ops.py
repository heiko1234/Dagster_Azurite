

import os
from pathlib import Path

from nycflights13 import flights

import pandas as pd
from dagster import op

# from data_pipeline_complex.resources import azurite_resource

# from data_pipeline_complex.utility import all_days, remove_fileformats, get_missing_dates



@op()
def container_name(context):
    context.log.info("Successful load container_name: azuriteblob")
    return "azuriteblob"


@op()
def sub_container_name(context):
    context.log.info("Successful load container_name: azuriteblob")
    return "flights"


@op()
def filetype_parquet(context):
    context.log.info("filetype: parquet")
    return "parquet"


@op(config_schema={"number_month": str})
def str_number(context):
    value = context.solid_config["number_month"]
    value_mod = int(value)+1
    context.log.info(f"number of the month: {value_mod}")
    return str(value_mod)


@op()
def split_flightdata(context, month):

    df = flights

    data = df[df["month"] == int(month)]

    return data


@op(required_resource_keys={"adls"})
def upload_data_to_blob(context, data, container_name, subcontainer, filename, filetype):
    relative_filename = f"./data/{subcontainer}/{filename}.{filetype}"
    file = Path(relative_filename)
    dir_to_create = file.parent
    os.makedirs(dir_to_create, exist_ok=True)
    if filetype == "csv":
        data.to_csv(relative_filename)
    if filetype == "parquet":
        data.to_parquet(relative_filename)
    
    context.log.info(f"successfully intermediate save {relative_filename}")

    client = context.resources.adls.blob_client.get_blob_client(
        container=container_name, blob = f"{subcontainer}/{filename}.{filetype}"
    )
    with file.open("rb") as data:
        client.upload_blob(data, overwrite=True)
    context.log.info(f"successfully written {filename} into blob")

    # remove temp file path
    Path(relative_filename).unlink()






