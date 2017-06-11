# Experimenting with visualisation of data used in our Code For Leipzig projects

## Set up
Use [docker-jupyter](https://github.com/lucasko-tw/docker-jupyter) as preconfigured Jupyter installation, i.e. `git clone https://github.com/lucasko-tw/docker-jupyter`.

Within the just locally cloned repository:
```
docker build -t jupyter:latest .
docker run --name jupyter_oklab -p 8888:8888 -e PASSWORD=<your_arbitrary_chosen_password> -d -it jupyter:latest /bin/bash -c "/opt/conda/bin/jupyter notebook --notebook-dir=/opt/notebooks --ip='*' --port=8888" 
```


## Logging in

Open `localhost:8888`, you should be able to login with the password used in the docker run command just before. If this doesn't work, you can also use `docker exec -it jupyter_oklab /bin/bash` and then within the docker container `jupyter notebook list` to get the link to the notebook inlcuding the access token. Also checkout [this page](http://jupyter-notebook.readthedocs.io/en/latest/security.html) for further information.


## On boarding

You can now start creating new notebooks or reuse one of those provided by this project.

Use the [iPython notebook tutorial](https://plot.ly/python/ipython-notebook-tutorial/#getting-started) to get started.

See also the [gallery of interesting Jupyter notebooks](https://github.com/jupyter/jupyter/wiki/A-gallery-of-interesting-Jupyter-Notebooks) as source of inspiration.


## Accessing resources from notebook

Note: if you're are working within a VirtualBox and want to access a database running in your VirtualBox from the Jupyter notebook just started as Docker container you have to use the IP address of the VirtualBox, this should be usually `10.0.2.15`.