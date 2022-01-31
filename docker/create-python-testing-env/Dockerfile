FROM ubuntu:focal

# Failsafe for tzdata
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Etc/UTC

# Add apt-add-repository and git to container
RUN apt-get update -y && apt-get -y install software-properties-common git

# Add a repo, then update the repo listing, then install python3.7, finally remove all repo listing
RUN apt-add-repository -y ppa:deadsnakes/ppa && apt-get update && \
    apt-get -y install python3.7 python3.7-venv python3.7-distutils && \
    rm -rf /var/lib/apt/lists/*

# Install (ensure) pip for Python
RUN python3.7 -m ensurepip

# Install pytest using pip
RUN python3.7 -m pip install pytest pytest-print