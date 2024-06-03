## To build image from Dockerfile use:
```
docker build . -t dl-test-container
```

## To create container use:
```
docker run --name dl-test-container -d -i -t dl-test-container /bin/sh
```
After that you can run tests:

```
docker exec dl-test-container python3 test/triposr_test.py
```

Or run application, that generates 3-d representation for images in examples:
```
docker exec dl-test-container ./createImagePath.sh
```

After that you should stop containet by yourself:
```
docker stop dl-test-container
docker rm dl-test-container
```

## To copy from docker to host:
```
docker cp dl-test-container:/app/output /tmp
```