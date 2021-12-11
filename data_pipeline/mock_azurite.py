
from azure.storage.blob import BlobServiceClient
from dagster import resource


@resource
def azurite_resource(init_context):
    storage_account = "devstoreaccount1"
    credential = (
        "Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw=="
    )
    return AzuriteResource(storage_account, credential)


# AZURE_STORAGE_CONNECTION_STRING="DefaultEndpointsProtocol=http;
#                        AccountName=devstoreaccount1;
#                        AccountKey=Eby8vdM02xNOcqFlqUwJPLlmEtlCDXJ1OUzFT50uSRZ6IFsuFq2UVErCz4I6tq/K1SZFPTOtr/KBHBeksoGMGw==;
#                        BlobEndpoint=http://localhost:10000/devstoreaccount1;
#                        QueueEndpoint=http://localhost:10001/devstoreaccount1"


class AzuriteResource:
    def __init__(self, storage_account, credential):
        connection_string = ";".join(
            [
                "DefaultEndpointsProtocol=http",
                f"AccountName={storage_account}",
                f"AccountKey={credential}",
                f"BlobEndpoint=http://127.0.0.1:10000/{storage_account}",
                f"QueueEndpoint=http://127.0.0.1:10001/{storage_account}",
            ]
        )
        self._blob_client = BlobServiceClient.from_connection_string(connection_string)
    
    @property
    def blob_client(self):
        return self._blob_client





