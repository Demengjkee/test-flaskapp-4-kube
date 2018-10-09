# test-flaskapp-4-kube

build:

`docker build -t <image-name> .`

run:

`docker run --rm -d -p 5000:5000 <image-name>`



`docker ps -f health=unhealthy`

`docker inspect --format=‘{{json .State.Health}}’ << container_name >>`
