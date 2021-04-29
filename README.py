Build the image
Now that we have a Dockerfile, let’s verify it builds correctly:

docker build -t flask-tutorial:latest .
After the build completes, we can run the container:

docker run -d -p 5000:5000 flask-tutorial

Simple Python Flask Dockerized Application#
Build the image using the following command

$ docker build -t simple-flask-app:latest .
Run the Docker container using the command shown below.

$ docker run -d -p 5000:5000 simple-flask-app
The application will be accessible at http:127.0.0.1:5000 or if you are using boot2docker then first find ip address using $ boot2docker ip and the use the ip http://<host_ip>:5000