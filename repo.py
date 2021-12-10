# repo.py

from dagster import job, op, repository, schedule, pipeline


@op
def get_name():
    return "dagster"


@op
def hello(context, name: str):
    context.log.info(f"Hello, {name}!")


@job
def hello_dagster():
    hello(get_name())


@schedule(cron_schedule="* * * * *", 
    job=hello_dagster, 
    execution_timezone="US/Central")
def my_schedule(_context):
    return {}


@repository
def deploy_docker_repository():
    return [hello_dagster, my_schedule]