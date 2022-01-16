


from data_pipeline_complex.resources import BlobStorageConnector

import dask
from dask.distributed import Client
from dask import delayed

import pandas as pd


import os

import datetime as dt


from dotenv import load_dotenv

load_dotenv()



connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING", "")
container_name = os.getenv("CONTAINER_NAME", "azuriteblob")

connection_string
container_name

sub_container_name = "flight"


client = BlobStorageConnector(container_name=container_name)

files_in_blob = client.list_files_in_subcontainer(subcontainer=sub_container_name, files_with=".parquet")

files_in_blob



# test single file load ;) works :)
file12 = client.get_parquet_file(subcontainer="flights", file="12.parquet")
file12



##############
##############


starttime=dt.datetime.now()
sums = []
counts = []


for f in files_in_blob:

    fn = client.get_parquet_file(subcontainer="flights", file=f)
    # Read in file
    # deplayed with dask:
    df = delayed(pd.read_parquet)(fn)
    # normal pandas
    #df = pd.read_csv(fn)

    # Groupby origin airport
    by_origin = df.groupby('origin')

    # Sum of all departure delays by origin
    total = by_origin.dep_delay.sum()

    # Number of flights by origin
    count = by_origin.dep_delay.count()

    # Save the intermediates
    sums.append(total)
    counts.append(count)


intertimeneeded = dt.datetime.now()-starttime
intertimeneeded.total_seconds()


# Compute the intermediates
sums, counts = dask.compute(sums, counts)

# Combine intermediates to get total mean-delay-per-origin
total_delays = sum(sums)
n_flights = sum(counts)
mean = total_delays / n_flights

timeneeded = dt.datetime.now()-starttime
timeneeded 


timeneeded.total_seconds()
intertimeneeded.total_seconds()




# pip install dask-azureblobfs
# No module named 'dask.bytes.local'
# install adlfs


from azureblobfs.dask import DaskAzureBlobFileSystem


import dask.dataframe as dd


account_name = os.getenv("AZURE_STORAGE_ACCOUNT")
account_key = os.getenv("AZURE_ACCOUNT_KEY")
connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING")


account_name
account_key 


data = dd.read_parquet("abfs://azuriteblob/flights/*.parquet",
    storage_options={"account_name": account_name,
        "account_key": account_key})

data


data2 = dd.read_parquet("abfs://azuriteblob/flights/*.parquet",
    storage_options={"connection_string": connection_string})

data2



starttime=dt.datetime.now()
sums = []
counts = []

intertimeneeded = dt.datetime.now()-starttime
intertimeneeded.total_seconds()

# Groupby origin airport
by_origin = data.groupby('origin')

# Sum of all departure delays by origin
total = by_origin.dep_delay.sum()

# Number of flights by origin
count = by_origin.dep_delay.count()

# Save the intermediates
sums.append(total)
counts.append(count)


# Compute the intermediates
sums, counts = dask.compute(sums, counts)

# Combine intermediates to get total mean-delay-per-origin
total_delays = sum(sums)
n_flights = sum(counts)
mean = total_delays / n_flights

#
total_delays
n_flights
mean

timeneeded = dt.datetime.now()-starttime
timeneeded.total_seconds()



# https://dask-azureblobfs.readthedocs.io/en/latest/usage.html

#data = dd.read_parquet("abfs://account_name/mycontainer/weather*.parquet",
#    storage_options={"account_name": account_name,
#        "account_key": account_key})

# AZURE_BLOB_ACCOUNT_NAME









