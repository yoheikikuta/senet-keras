FROM nvidia/cuda:8.0-cudnn6-devel-ubuntu16.04
MAINTAINER Yohei Kikuta <yohei-kikuta@cookpad.com>

# Install git, wget, bc and dependencies
RUN apt-get update && apt-get install -y \
    iproute2 \
    python3.5 \
    python3-pip \
    python3-dev

RUN pip3 install --upgrade pip

# Install python modules.
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

# assume ubuntu user id is 1000.
RUN useradd docker -u 1000 -s /bin/bash -m
USER docker

# Set alias for python3.5
RUN echo "alias python=python3" >> $HOME/.bashrc && \
    echo "alias pip=pip3" >> $HOME/.bashrc

WORKDIR /work
RUN ["/bin/bash"]
