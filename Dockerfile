FROM python:3.9-slim
RUN wget -qO- https://ipecho.net/plain ; echo
RUN pip install locust==2.16.1

COPY locustfile.py /locustfile.py
COPY entrypoint.sh /entrypoint.sh
COPY requirements.txt /requirements.txt

ENTRYPOINT ["/entrypoint.sh"]
