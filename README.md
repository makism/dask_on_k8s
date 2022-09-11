
# Prerequisties

1. k8s cluster using minikube
2. conda env with python 3.9 and,
3. dask and dask_kubernetes installed


# k8s

Fetch `minikube` from https://minikube.sigs.k8s.io/docs/start/.
Spin a k8s cluster using

```
minikube config set vm-driver docker
minikube start --memory 16000 --cpus=8
```

as soon as it is up, start the dashboard with

```
minikube dashboard
```

You may watch the pods in the cluster with:
```
watch -n1 "minikube kubectl -- get pods -A -o wide
```

# Python packages

Preferably create a new conda env with python 3.9 and install the following packages:
* dask: ```conda install dask```
* dask-kubernetes with: ```conda install dask-kubernetes -c conda-forge```

# Example

The following example is taken from https://kubernetes.dask.org/en/latest/kubecluster.html:

```python
from dask_kubernetes import KubeCluster, make_pod_spec

pod_spec = make_pod_spec(
    image="ghcr.io/dask/dask:latest",
    memory_limit="1G",
    memory_request="1G",
    cpu_limit=1,
    cpu_request=1,
)

cluster = KubeCluster(pod_spec)

cluster.scale(10)  # specify number of workers explicitly
cluster.adapt(minimum=1, maximum=100)  # or dynamically scale based on current workload


# Example usage
from dask.distributed import Client
import dask.array as da

# Connect Dask to the cluster
client = Client(cluster)

# Create a large array and calculate the mean
array = da.ones((1000, 1000, 1000))
print(array.mean().compute())  # Should print 1.0

```
