# Start a Jupyter hub instance

## Setup

```
sudo docker build --tag leipzig-jupyterhub .
sudo docker run -p 8083:8000 -d --name jupyterhub leipzig-jupyterhub jupyterhub
# check if server is running without errors
sudo docker logs jupyterhub
# connect to running server instance
sudo docker exec -it jupyterhub bash
# set a password for the user
passwd joerg
# replace x.x.x.x with the IP of your host machine
echo "x.x.x.x 127.0.0.1" >> /etc/hosts
```

Open <myserver>:8083 in your browser, login with credentials joerg and the just created password.

Then hit `Start server`.

Navigate into folder `notebooks` and either select New to create a new Python 3 notebook or select Upload to upload an existing ipynb file.

## To be solved
 * configure Apache reverse proxy to allow web socket connection to Jupyter kernels


