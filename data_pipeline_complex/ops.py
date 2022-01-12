
import os
from pathlib import Path


from nycflights13 import flights


# from typing import Container

import pandas as pd
from dagster import op
from data_pipeline_complex.resources import azurite_resource

from data_pipeline_complex.utility import all_days, remove_fileformats, get_missing_dates



@op()
def container_name(context):
    context.log.info("Successful load container_name: azuriteblob")
    return "azuriteblob"




@op()
def split_data(month):

    df = flights

    data = df[df["month"] == month]

    return data



@op(required_resource_keys={"adls"})
def upload_data_to_blob(data):







