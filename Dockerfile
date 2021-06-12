FROM python:alpine

WORKDIR /root/viewdns-python
ADD requirements.txt requirements.txt
RUN pip3 install -U -r requirements.txt

ADD . /root/viewdns-python

CMD python3 -m pytest