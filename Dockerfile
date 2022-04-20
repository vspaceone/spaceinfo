# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

# Install git
RUN apt-get update
RUN apt-get install git cron -y

# Create user
ARG user=appuser
ARG group=appuser
ARG uid=1000
ARG gid=1000
RUN groupadd -g ${gid} ${group}
RUN useradd -u ${uid} -g ${group} -s /bin/sh -m ${user}

# Switch to user
USER ${uid}:${gid}

# Clone pages repository. Setup your repository here!
WORKDIR /home/${user}/

RUN ls
RUN pwd

RUN git clone https://github.com/vspaceone/spaceinfo-pages
RUN git -C /home/${user}/spaceinfo-pages pull origin master
RUN echo "16 * * * * git -C /home/${user}/spaceinfo-pages pull origin master" >> cron.txt
RUN crontab cron.txt

# Setup the python environment
WORKDIR /home/${user}/spaceinfoserver
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

# Copy files into the container
COPY . .

# Expose port
EXPOSE 5000

# Run python
CMD [ "bash", "run.sh" ]