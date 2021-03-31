# DockerPerformanceTesting
This project is compatible with all the docker registry and capable to doing a performance test with sequential pulls  

# Tested with Harbor Sequential Pulls Perf testing 

Ensure docker is installed in the Host Machine 
[Docker installation](https://docs.docker.com/engine/install/)

```pip3 install docker```

Make sure to change before you run  

image name to the desired image that needs to be pulled 
count refers to the no of times image needs to pulled

```
imagename="docker.io/library/busybox:latest"
count=2
```

```python3 dockerpull.py --imagename=<imagename> --count=<count>```
