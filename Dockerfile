FROM quay.io/acb-fr/qiot-sensor-service-base:1.0.0

LABEL maintainer="Rémi VERCHERE <remi.verchere@axians.com>"
LABEL version="0.1"

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "./app.py" ]

