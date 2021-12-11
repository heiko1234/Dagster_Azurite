# Dagster_Azurite


connect to pre existing network with azurite for mlflow
https://tjtelan.com/blog/how-to-link-multiple-docker-compose-via-network/
https://training.play-with-docker.com/docker-networking-hol/




# works
docker exec -it blob ping docker_example_user_code
PING docker_example_user_code (172.21.0.4): 56 data bytes
64 bytes from 172.21.0.4: seq=0 ttl=64 time=0.116 ms

# works
in dockerfile: 
    RUN apt-get update
    RUN apt-get install inetutils-ping

docker exec -it docker_example_user_code ping blob

# not yet
docker exec -it docker_example_dagit ping blob



docker exec -it docker_example_user_code ping blob



docker network inspect general_nw

docker network inspect docker_example_network



docker_example_user_code

docker_example_dagit

postgres




