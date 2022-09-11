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
