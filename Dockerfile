# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

# Install git
RUN apt-get update
RUN apt-get install git -y

# Clone pages repository. Setup your repository here!
RUN git clone https://github.com/vspaceone/spaceinfo-pages

# Setup the python environment
WORKDIR /spaceinfoserver
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# Copy files into the container
COPY . .

# Expose port
EXPOSE 5000

# Run python
CMD [ "bash", "run.sh" ]