FROM python:3.8.3-buster

RUN pip install locust

COPY locustfile.py /locustfile.py
COPY entrypoint.sh /entrypoint.sh
COPY requirements.txt /requirements.txt

ENTRYPOINT ["/entrypoint.sh"]
