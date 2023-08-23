pip-install:
	podman build -t my-jupyterhub-image .
django-serve:
	podman run -d -p 8000:8000 my-jupyterhub-image
