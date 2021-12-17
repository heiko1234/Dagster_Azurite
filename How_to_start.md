
# Power Shell
# this
Set-Variable -Name "DAGSTER_HOME" -value "./.dagster"
Get-Variable -Name "DAGSTER_HOME"

# Ubuntu 
# export DAGSTER_HOME=./.dagster
# export DAGSTER_HOME="./.dagster_home"
# need to be absolute path

# works in bash
export DAGSTER_HOME="/home/heiko/Repos/dagster_azurite/.dagster"
## this
dagster-daemon run


# in docker container
ENV PATH=/opt/dagster/app/.venv/bin:$PATH
ENV DAGSTER_HOME=/opt/dagster/app/dagster_home


RUN mkdir -p $DAGSTER_HOME
COPY dagster.yaml $DAGSTER_HOME


# works in bash
dagit -m repository
## this
dagit -f repository.py



# PowerShell
# $env:DAGSTER_HOME = './.dagster_home'
# or have all stuff in .env file



docker build -t docker_dagster .
docker-compose build


docker-compose up --build


docker-compose down -v


# dagster api grpc -f ./data_pipeline/jobs.py --host 0.0.0.0 --port 3030


dagster-daemon run

dagit -f ./data_pipeline/jobs.py --host 0.0.0.0 --port 3030

dagit -m repository.py --host 0.0.0.0 --port 3030

# seem not to work
# dagit -m repository --host 0.0.0.0 --port 3030



# works in bash
dagit -m repository

# Dagster_Azurite


connect to pre existing network with azurite for mlflow
https://tjtelan.com/blog/how-to-link-multiple-docker-compose-via-network/
https://training.play-with-docker.com/docker-networking-hol/




# works
docker exec -it blob ping docker_example_user_code
# result
PING docker_example_user_code (172.21.0.4): 56 data bytes
64 bytes from 172.21.0.4: seq=0 ttl=64 time=0.116 ms

# works
in dockerfile: 
    RUN apt-get update
    RUN apt-get install inetutils-ping

docker exec -it docker_example_user_code ping blob
# result
PING blob (172.21.0.3): 56 data bytes
64 bytes from 172.21.0.3: icmp_seq=0 ttl=64 time=0.049 ms

# not yet
docker exec -it docker_example_dagit ping blob

# ping from normal laptop
ping -c5 172.21.0.3  # works to connect to blob



docker exec -it docker_example_user_code ping blob



docker network inspect general_nw

                "Name": "blob",
                "EndpointID": "f92be71bcea8b0f846b2251a9d2b3c312ef102fbd2d6a3855658cf773cc60aaa",
                "MacAddress": "02:42:ac:15:00:03",
                "IPv4Address": "172.21.0.3/16",

docker network inspect docker_example_network



docker_example_user_code

docker_example_dagit

postgres



