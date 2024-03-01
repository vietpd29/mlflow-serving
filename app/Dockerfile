# pull openjdk 8
FROM ubuntu:22.04

# Update package repositories and install JDK 8 and Python 3.9
RUN apt-get update && \
    apt-get install -y openjdk-8-jdk python3-pip

# Set the JAVA_HOME environment variable
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64

# set workdir
WORKDIR /serving

# copy requirements to workdir
COPY requirements.txt /serving/requirements.txt

# install all requirement
RUN pip install --no-cache-dir --upgrade -r /serving/requirements.txt

# copy code to workdir
COPY . /serving/app

# run the app
CMD python3 app/main.py
