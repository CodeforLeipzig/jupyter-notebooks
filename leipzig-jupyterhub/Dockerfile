FROM jupyterhub/jupyterhub:latest

RUN pip install ipython && pip install --upgrade jupyter --ignore-installed

RUN useradd -ms /bin/bash joerg && mkdir /home/joerg/notebooks && chown -R joerg /home/joerg/notebooks

COPY ./jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py
