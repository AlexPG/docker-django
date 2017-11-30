FROM python:3.6
COPY requirements.txt /tmp/requirements.txt
RUN pip install -qr /tmp/requirements.txt
COPY . /src/
WORKDIR /src