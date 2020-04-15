FROM python:3.6-slim

# update system
RUN apt-get update -qq \
 && apt-get upgrade -y \
 && apt-get install build-essential -y \
 && apt-get autoremove -y

# set working directory
WORKDIR /app

# copy dependencies file
COPY ./requirements.txt /app/requirements.txt

# install dependencies
RUN python -m venv /opt/venv \
  && . /opt/venv/bin/activate \
  && pip install --upgrade pip \
  && pip install --no-cache-dir rasa pycountry us

# copy source
COPY . /app

# train the model
RUN . /opt/venv/bin/activate && rasa train


