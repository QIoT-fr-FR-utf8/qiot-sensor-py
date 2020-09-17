FROM quay.io/acb-fr/qiot-sensor-service-base:1.0.0

LABEL app="QIoT project"
LABEL maintener="David AUFFRAY <david.auffray@axians.com>"
LABEL major_version="1"
LABEL minor_version="0"

WORKDIR /usr/src/app

COPY requirements.txt ./

ENV FLASK_APP /usr/src/app/app.py
ENV APP_PORT 8000
ENV APP_HOST "0.0.0.0"
ENV APP_DEBUG "False"

COPY . .

RUN /bin/bash --help


CMD [ "/bin/bash" ]