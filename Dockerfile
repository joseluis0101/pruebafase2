
FROM python:3.6

ENV PYTHONUNBUFFERED 1

COPY . /code/
WORKDIR /code/

MAINTAINER jose_luis

RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip install --upgrade pip
RUN apt-get install -y python3-dev
RUN apt-get install -y python3 python3-pip python3-dev
RUN apt-get install -y libxml2-dev libxslt-dev libffi-dev libssl-dev
RUN apt-get install -y default-libmysqlclient-dev
RUN apt-get install -y gettext nginx vim

RUN pip install -r requirements.txt
RUN python manage.py collectstatic --noinput

#RUN python manage.py runserver 0.0.0.0:8080

# Add source code.
#ADD . /code/

# Run script file.
#CMD ./run.sh
EXPOSE 8080
