c.JupyterHub.ip = '0.0.0.0'
c.JupyterHub.port = 8000

# Use DummyAuthenticator for testing purposes
from jupyterhub.auth import DummyAuthenticator
c.JupyterHub.authenticator_class = DummyAuthenticator

# Allow named users to access JupyterHub
c.Authenticator.allowed_users = {'user1', 'user2'}

# Use the DockerSpawner to spawn user notebooks in containers
from dockerspawner import DockerSpawner
c.JupyterHub.spawner_class = DockerSpawner
c.DockerSpawner.image = 'jupyter/base-notebook'

# Configure the location for user data persistence
c.DockerSpawner.notebook_dir = '/home/jovyan/work'

# Set resource limits for user containers
c.DockerSpawner.mem_limit = '1G'
c.DockerSpawner.cpu_limit = 1.0

# Use the default HubAuth and LocalProcessSpawner for single-user servers
c.JupyterHub.hub_connect_ip = 'jupyterhub'
