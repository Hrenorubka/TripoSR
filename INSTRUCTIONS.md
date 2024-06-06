## To build image from Dockerfile use:
```
docker build . -t dl-test-container
```
This command creates image with name `dl-test-container`. Commands below use this name of image.

## To create container with name `dl-test-container` use:
```
docker run --name dl-test-container -d -i -t dl-test-container /bin/sh
```
After that you can run tests:

```
docker exec dl-test-container python3 test/triposr_test.py
```

Or run application, that generates 3-d representation for images in [image_to_compute](./image_to_compute) folder:
```
docker exec dl-test-container ./createImagePath.sh
```

After all done in container, you should stop container by yourself:
```
docker stop dl-test-container
docker rm dl-test-container
```

## To copy output from docker to host use command:
```
docker cp dl-test-container:/app/output /tmp
```