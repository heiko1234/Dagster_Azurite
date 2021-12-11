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




