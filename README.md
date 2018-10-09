# test-flaskapp-4-kube

## Description
This is an example of the simplest application to fail by request.
Application is supposed to start (be ready) in 30 sec after creation.

## HOWTO

### Build
```
docker build -t << image-name >> .
```

### Run
```
docker run --rm -d -p 5000:5000 << image-name >>
```

### Check Status
```
# Get unhealthy containers
docker ps -f health=unhealthy

# Get Helath status of the given contanier
docker inspect --format='{{json .State.Health}}' << container_name >>
```

### Getting Logs
```
# One-shot logs
docker logs << container_name >>

# Polling Logs
docker logs -f << container_name >>
```
