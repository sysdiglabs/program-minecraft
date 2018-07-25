FROM python:3.6

WORKDIR /usr/src/app

RUN git clone https://github.com/py3minepi/py3minepi && pip install --no-cache-dir py3minepi/ && rm -fr py3minepi

CMD [ "python" ]