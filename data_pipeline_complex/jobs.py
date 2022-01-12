

from importlib import resources
from dagster import ModeDefinition, job 

from data_pipeline_complex.resources import azurite_resource


from data_pipeline_complex.ops import container_name
from data_pipeline_complex.ops import split_data
from data_pipeline_complex.ops import container_name






local_blob_mode = ModeDefinition(
    "azurite_blob", 
    resource_defs={
        "adls": azurite_resource
    }
)


@job(resource_defs={"adls": azurite_resource})
def sensor_data_to_blob():
    containername = container_name()










