FROM python:3.9-slim

RUN pip install locust==2.16.1

COPY locustfile.py /locustfile.py
COPY entrypoint.sh /entrypoint.sh
COPY requirements.txt /requirements.txt

ENTRYPOINT ["/entrypoint.sh"]
