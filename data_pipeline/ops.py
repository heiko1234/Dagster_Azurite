import os
from pathlib import Path
# from typing import Container

import pandas as pd
from dagster import op


@op()
def name_sting(context):
    context.log.info("Successful load name_string")
    # filename = "sampledata/sampledata.csv"
    return "sampledata/sampledata.csv"


@op()
def container_name(context):
    context.log.info("Successful load container_name")
    return "azuriteblob"


@op()
def where_to_safe(context):
    context.log.info("Successful load where_to_safe")
    return "targetfolder/output_sampledata.csv"


@op(required_resource_keys={"adls"})
def load_csv_from_blob(
    context,
    container_name,
    filename
):

    context.log.info(f"Init load csv from blob")
    client = context.resources.adls.blob_client.get_blob_client(
        container=container_name, blob=filename
    )
    context.log.info(f"Successfully initiated client")
    dir_to_create = "".join(filename.split("/")[0:-1])
    # dir_to_create = "data_folder"
    os.makedirs(dir_to_create, exist_ok=True)
    context.log.info(f"Successfully checked dir: {dir_to_create}")
    with open(filename, "wb") as file:
        blob_data = client.download_blob()
        blob_data.readinto(file)
    context.log.info(f"Successfully saved downloaded file")
    df = pd.read_csv(filename, sep=";")
    context.log.info(f"Successful loaded file: {filename}")
    Path(filename).unlink()

    return df


@op(required_resource_keys={"adls"})
def upload_data_to_blob(
    context,
    df,
    container_name,
    filename
):
    relative_filename = f"./data/{filename}"
    file = Path(relative_filename)
    dir_to_create = file.parent
    os.makedirs(dir_to_create, exist_ok=True)
    # save df locally
    df.to_csv(relative_filename)
    context.log.info(f"Successfully in docker save: {filename}")
    # upload file to blob
    client = context.resources.adls.blob_client.get_blob_client(
        container= container_name, blob = filename
    )
    with file.open("rb") as data:
        client.upload_blob(data, overwrite = True)
    context.log.info(f"Successfully wrote {filename} in blob")
    # remove local temporary file
    Path(relative_filename).unlink()
    context.log.info(f"Successfully deleated local docker: {file}")


