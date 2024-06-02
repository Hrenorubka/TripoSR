## To build image from Dockerfile use:
```
docker build . -t dl-test-container
```

## To create container and run app on it use: 
```
docker run --name dl-test-container dl-test-container
```

## To copy from docker to host:
```
docker cp dl-test-container:/app/out /tmp
```
