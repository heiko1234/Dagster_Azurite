


import os

from azure.storage.blob import BlobServiceClient
from azure.storage.blob import ContainerClient
from dagster import resource

from dotenv import load_dotenv

from data_pipeline.ops import container_name
load_dotenv()


@resource
def azurite_resource(init_context):
    storage_account = "devstoreaccount1"
    credential = (
        "Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw=="
    )
    return AzuriteResource(storage_account, credential)



class AzuriteResource:
    def __init__(self, storage_account, credential):
        connection_string = ";".join(
            [
                "DefaultEndpointsProtocol=http",
                f"AccountName={storage_account}",
                f"AccountKey={credential}",
                f"DefaultEndpointsProtocol=http",
                f"BlobEndpoint=http://127.0.0.1:10000/{storage_account}",
                f"QueueEndpoint=http://127.0.0.1:10001/{storage_account}",
            ]
        )
        self._blob_client = BlobServiceClient.from_connection_string(connection_string)
    
    @property
    def blob_client(self):
        return self._blob_client



class BlobStorageConnector:
    """Clas for connecting to blob storage using Azure Connection String"""

    def __init__(self, container_name: str):
        self.__container = container_name
        self.connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING", "")
        # account_name = os.environ["AZURE_STORAGE_NAME"]
    
    def get_container_client(self):
        blob_container_client = ContainerClient.from_connection_string(
            self.connection_string, container_name=self.__container)
        return blob_container_client
    
    def list_files_in_subcontainer(self,subcontainer, file):
        output = []
        for blob in get_container_client().list_blobs():
            if subcontainer in blob.name and file in blob.name:
                output.append(blob.name.split("/")[1])
        return output



def get_container_client(container_name="azuriteblob"):
    return BlobStorageConnector(container_name=container_name).get_container_client()



def get_list_files_in_subcontainer(container_name="azuriteblob", subcontainer="targetfolder", file=".csv"):

    output = []

    for blob in get_container_client().list_blobs():
        if subcontainer in blob.name and ".csv" in blob.name:
            output.append(blob.name.split("/")[1])
    return output





BlobStorageConnector(container_name="azuriteblob").list_files_in_subcontainer(subcontainer="targetfolder", file = ".csv")


get_list_files_in_subcontainer(container_name="azuriteblob", subcontainer="targetfolder", file=".csv")
