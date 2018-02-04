from IPython.utils.localinterfaces import public_ips
c.JupyterHub.hub_ip = public_ips()[0]
#c.JupyterHub.hub_ip = '172.18.0.1'

c.JupyterHub.proxy_api_ip = '0.0.0.0'
c.DockerSpawner.container_ip = '0.0.0.0'
c.DockerSpawner.use_internal_ip = False

# Set the log level by value or name.
c.JupyterHub.log_level = 'DEBUG'

# Enable debug-logging of the single-user server
c.Spawner.debug = True

# Enable debug-logging of the single-user server
c.LocalProcessSpawner.debug = True

c.SudoSpawner.debug_mediator = True

