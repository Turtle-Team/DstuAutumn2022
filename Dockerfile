FROM python:3.10-slim-buster
MAINTAINER Turtle Team 'Alexey Shashkin'
COPY server /server
COPY requirements.txt requirements.txt
ADD ./ server/
ENV PATH=$PATH:/server
ENV PYTHONPATH /server
RUN pip3 install -r requirements.txt
CMD ["python3", "server/main.py"]

