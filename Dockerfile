FROM python:3.10-buster

RUN useradd -ms /bin/bash app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

ENV APP_HOME=/home/app
WORKDIR $APP_HOME

COPY requirements.txt ./

RUN apt-get update -y 
RUN apt-get clean -y

RUN pip install --no-cache --upgrade pip
RUN pip install -r requirements.txt

# RUN chown -R app:app $APP_HOME

# change to the app user
# USER app
