FROM nvidia/cuda:9.0-cudnn7-devel-ubuntu16.04
LABEL maintainer="diracdiego@gmail.com"
LABEL version="2.0"

# Install git, wget, bc and dependencies
RUN apt-get update && apt-get install -y \
    iproute2 \
    python3.5 \
    python3-pip \
    python3-dev

RUN pip3 install --upgrade pip

# Install python modules.
COPY ./requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt

# Set alias for python3.5
RUN echo "alias python=python3" >> $HOME/.bashrc && \
    echo "alias pip=pip3" >> $HOME/.bashrc

WORKDIR /work
RUN ["/bin/bash"]
