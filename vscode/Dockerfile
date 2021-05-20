FROM codercom/code-server:3.8.1

MAINTAINER angel@molanco.com

USER root

RUN apt-get update

RUN apt-get install wget -y

RUN wget https://bootstrap.pypa.io/get-pip.py

RUN apt-get install python3-distutils -y

RUN python3 get-pip.py --prefix=/usr/local/ --disable-pip-version-check --no-cache-dir

RUN rm -f get-pip.py

WORKDIR /vscode

# RUN git clone https://github.com/py3minepi/py3minepi really old version
RUN git clone https://github.com/martinohanlon/mcpi

RUN pip3 install --no-cache-dir mcpi/ && rm -fr mcpi

# https://minecraft-stuff.readthedocs.io/en/latest/minecraftshape.html
RUN pip3 install minecraftstuff

RUN chown coder:coder /vscode

USER coder