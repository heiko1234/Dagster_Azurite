
# Power Shell
Set-Variable -Name "DAGSTER_HOME" -value "./.dagster"
Get-Variable -Name "DAGSTER_HOME"

# Ubuntu 
# export DAGSTER_HOME=./.dagster
# export DAGSTER_HOME="./.dagster_home"
# need to be absolute path

# works in bash
export DAGSTER_HOME="/home/heiko/Repos/dagster_azurite/.dagster"
dagster-daemon run


# in docker container
ENV PATH=/opt/dagster/app/.venv/bin:$PATH
ENV DAGSTER_HOME=/opt/dagster/app/dagster_home


RUN mkdir -p $DAGSTER_HOME
COPY dagster.yaml $DAGSTER_HOME


# works in bash
dagit -m repository
dagit -f repository.py



# PowerShell
# $env:DAGSTER_HOME = './.dagster_home'
# or have all stuff in .env file



docker build -t docker_dagster .
docker-compose build


docker-compose up --build


# dagster api grpc -f ./data_pipeline/jobs.py --host 0.0.0.0 --port 3030


dagster-daemon run

dagit -f ./data_pipeline/jobs.py --host 0.0.0.0 --port 3030

dagit -m repository.py --host 0.0.0.0 --port 3030

# seem not to work
# dagit -m repository --host 0.0.0.0 --port 3030



# works in bash
dagit -m repository

