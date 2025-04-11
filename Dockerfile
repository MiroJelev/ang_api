# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.11.2

ENV PYTHONUNBUFFERED=1
ENV DIRPATH=/usr/local/app

ENV SQL_HOST=$SQL_HOST
ENV SQL_PORT=$SQL_PORT
ENV SQL_USER=$SQL_USER
ENV SQL_PASS=$SQL_PASS

WORKDIR $DIRPATH

RUN apt update -y & apt upgrade -y

COPY ./ /usr/local/app/

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]