FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /home/web
WORKDIR /home/web

RUN pip3 install pip -U
ADD requirements.txt /home/web/requirements.txt
RUN pip3 install -r requirements.txt

ADD . /home/web

