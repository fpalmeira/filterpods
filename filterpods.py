from kubernetes import client, config
from kubernetes.client.rest import ApiException
import os
import sys

phase = os.environ['POD_STATUS']

def list_pods_by_status_state(phase):
    config.load_incluster_config()
    v1 = client.CoreV1Api()

    try:
        print(f"Listing all pods with status: {phase}")
        all_pods = v1.list_pod_for_all_namespaces(watch=False)
        print("%s\t%s" % ("Pod name", "Pod namespace"))
        for pod in all_pods.items:
            pod_phase=pod.status.phase
            if phase in pod_phase:
                print("%s\t%s" % (pod.metadata.name, pod.metadata.namespace))

    except ApiException as e:
        print(f"Exception when calling CoreV1Api->list_pod_for_all_namespaces: {e}\n")
        sys.exit(1)

    
if __name__ == "__main__":
    list_pods_by_status_state(phase)
