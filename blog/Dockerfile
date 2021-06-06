# pull official base image
FROM python:3.9.5-buster
# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#RUN apk update
#RUN apk add postgresql-dev gcc python3-dev musl-dev zlib-dev jpeg-dev

ADD . /usr/src/app

# install depenencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

#CMD python manage.py runserver -h 0.0.0.0
