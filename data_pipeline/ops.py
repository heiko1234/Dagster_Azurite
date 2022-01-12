import os
from pathlib import Path
# from typing import Container

import pandas as pd
from dagster import op


@op()
def local_name_string(context):
    context.log.info("Successful load name_string")
    # filename = "sampledata/sampledata.csv"
    return "./sampledata_folder/sampledata.csv"
    # return "sampledata.csv"


@op()
def blob_name_string(context):
    context.log.info("Successful load name_string: sampledata_folder/sampledata.csv")
    # filename = "sampledata/sampledata.csv"
    return "sampledata_folder/sampledata.csv"
    # return "sampledata.csv"


@op()
def container_name(context):
    context.log.info("Successful load container_name: azuriteblob")
    return "azuriteblob"


@op()
def blob_where_to_safe(context):
    context.log.info("Successful load where_to_safe: targetfolder/output_sampledata.csv")
    return "targetfolder/output_sampledata.csv"


@op()
def local_dump_data(context, data, path):
    context.log.info("Successful dump data locally")
    context.log.info(f"path: {path}")
    context.log.info(f"data: {data}")

    data.to_csv(path)



@op()
def call_local_data(context, path):
    context.log.info("Succesful load local data")
    # datapath = "./sampledata_folder/sampledata.csv"
    datapath = path
    data = pd.read_csv(datapath, sep = ",")
    context.log.info(f"data: {data}")
    return data


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
    try: 
        dir_to_create = "".join(filename.split("/")[0:-1])
        # dir_to_create = "data_folder"
        os.makedirs(dir_to_create, exist_ok=True)
        context.log.info(f"Successfully checked dir: {dir_to_create}")
        os.listdir()
    except BaseException:
        pass

    context.log.info(f"Check folder: {os.listdir()}")
    context.log.info(f"Successfully checked container_name: {container_name}")
    context.log.info(f"Successfully checked filename: {filename}")
    
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


@op()
def sensor_op(context, data):
    context.log.info(f"data: {data}")
    a = data.iloc[-1:,:] + 1
    df = data.append(a, ignore_index=True)
    context.log.info(f"new df: {df}")

    return df




