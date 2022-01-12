
import os
from pathlib import Path
# from typing import Container

import pandas as pd
from dagster import op
from data_pipeline_complex.resources import azurite_resource



@op()
def container_name(context):
    context.log.info("Successful load container_name: azuriteblob")
    return "azuriteblob"










