


import datetime as dt

import pandas as pd
from dagster import RunRequest, schedule, sensor








#@schedule(cron_schedule="* * * * *", 
#    job=hello_dagster, 
#    execution_timezone="US/Central")
#def my_schedule(context):
#    return {}


@sensor(pipeline_name="dagster_pipeline_sensor", minimum_interval_seconds=30)
def sensor_data_change(context):

    last_mod_time = float(context.cursor) if context.cursor else 0

    # "/home/heiko/Repos/dagster_azurite/sampledata_folder/sampledata.csv"
    datapath = "./sampledata_folder/sampledata.csv"
    data= pd.read_csv(datapath)
    current_index_number = max(data.iloc[:,0])
    # current_index_number

    if int(current_index_number) == int(last_mod_time):
        return False

    # not more than 20 indexes
    if int(current_index_number)  >= 20:
        return False #noqa

    yield RunRequest(
        run_key=f"updated_timestamp_{last_mod_time}",
        run_config={
            #"solids":{
            #    "sensor_op":{},
            #}
        }
    )
    context.update_cursor(str(last_mod_time))




