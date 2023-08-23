# Use a base image with Python and JupyterHub pre-installed
FROM jupyterhub/jupyterhub:latest

# Install any additional dependencies or packages here
# For example, if you need specific libraries for your notebooks
RUN pip install numpy pandas matplotlib dockerspawner

# Copy your JupyterHub configuration file into the container
COPY jupyterhub_config.py /srv/jupyterhub/jupyterhub_config.py

# Expose the port that JupyterHub will run on
EXPOSE 8000

# Start JupyterHub
CMD ["jupyterhub", "-f", "/srv/jupyterhub/jupyterhub_config.py"]
