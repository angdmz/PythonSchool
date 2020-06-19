FROM python:3.8.3-alpine3.12
RUN mkdir -p /opt/project
WORKDIR /opt/project
COPY requirements.txt /opt/project
RUN pip install -U pip
RUN pip install -r requirements.txt
RUN pip install ipython
RUN pip install attrdict