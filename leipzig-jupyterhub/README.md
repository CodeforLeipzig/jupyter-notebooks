# Start a Jupyter hub instance

## Setup

### Preparation

When jupyterhub should be able to access an data source from a different docker container, e.g. a started elasticsearch docker container:

```
# after starting the docker container, display docker network, just use the name of the first bridged network (usually "bidged") to use it in place of <docker-network-name> in the next command
sudo docker network ls
# after executing the following command look in its output for the internal ip address of the docker container you want access later from jupyterhub
sudo docker inspect <docker-network-name>
# for getting the internal ip address for docker host within the docker network use this command (only required if you want to address something running at your docker host directly):
sudo ip addr show docker0
```

```
sudo docker build --tag leipzig-jupyterhub .
# replace <docker-network-name> with the actual network name to start jupyterhub dockerhub container in the very same docker network
sudo docker run --net <docker-network-name> -p 8083:8000 -d --name jupyterhub leipzig-jupyterhub jupyterhub
# check if server is running without errors
sudo docker logs jupyterhub
# connect to running server instance
sudo docker exec -it jupyterhub bash
# set a password for the user
passwd joerg
# replace x.x.x.x with the IP of your host machine
echo "x.x.x.x 127.0.0.1" >> /etc/hosts
# install some additional python libraries to be access elasticsearch as well as do calculations and drawing charts
pip install elasticsearch
pip install matplotlib
pip install pandas
exit
```

Open <myserver>:8083 in your browser, login with credentials joerg and the just created password.

Then hit `Start server`.

Navigate into folder `notebooks` and either select New to create a new Python 3 notebook or select Upload to upload an existing ipynb file.

For accessing elasticsearch from notbook use the before retrieved internal ip address of the elasticsearch docker container.
