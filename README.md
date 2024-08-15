# filterpods
Repository for the filterpods app
The lastest image used by the Python app is stored in the Docker Hub registry
https://hub.docker.com/r/ltwistz/filterpods

The python script was deployed to a docker image through a Dockerfile and then the image was pushed to the registry.
Then I created the necessary resources so the pod executing this code in a K3D (fastest one I could think of) so it could have access to cluster info. 
Then created a helm chart to deploy it easier.

Hope you enjoy it.