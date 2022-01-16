

import pandas as pd
import os


from azure.storage.blob import BlobServiceClient

from dotenv import load_dotenv

load_dotenv()


def check_blobfiles(connection_string, container_name, sub_container=None, file=None):

    bsclient = BlobServiceClient.from_connection_string(
        connection_string
    )

    container_client = bsclient.get_container_client(container_name)

    output = []

    for blob in container_client.list_blobs():
        
        if sub_container:
            if sub_container in blob.name and file in blob.name:
                print(f"found: {blob.name}")
                output.append(blob.name.split("/")[1])
        if not sub_container:
            if file in blob.name:
                print(f"found: blob.name")
                output.append(blob.name)
    return output


connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING", "")
container_name = os.getenv("CONTAINER_NAME", "azuriteblob")

connection_string
container_name


list_parquet_blobfiles = check_blobfiles(connection_string=connection_string,
                                    container_name=container_name,
                                    sub_container="sampledata_folder",
                                    file=".parquet")


list_parquet_blobfiles  #empty


list_csv_blobfiles = check_blobfiles(connection_string=connection_string,
                                    container_name=container_name,
                                    sub_container="sampledata_folder",
                                    file=".csv")


list_csv_blobfiles   # sampledata.csv




list_parquet_blobfiles = check_blobfiles(connection_string=connection_string,
                                    container_name=container_name,
                                    sub_container="flights",
                                    file=".parquet")


list_parquet_blobfiles  #

len(list_parquet_blobfiles)  #12

