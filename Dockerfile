FROM quay.io/acb-fr/qiot-sensor-service-base:1.0.0
#FROM python:3.8.5

LABEL maintainer="Rémi VERCHERE <remi.verchere@axians.com>"
LABEL version="0.1"


WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./app.py" ]

EXPOSE 8000/tcp
