# Using ubuntu 18.04 as base
FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa && \
    apt-get update && \
    DEBIAN_FRONTEND="noninteractive" apt-get install -y python3-pip python3.9 python3.9-dev python3.9-distutils

# set a directory for the app
WORKDIR /usr/src/app

COPY ./requirements.txt .

# install dependencies
RUN python3.9 -m pip install --no-cache-dir -r requirements.txt

# copy all the files in the same folder as the Dockerfile to the container
COPY . .

ENTRYPOINT ["/usr/bin/nohup", "python3.9", "hello.py"]
