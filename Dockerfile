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

RUN dnf search make
RUN dnf install make -y
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "uvicorn", "app:app","--host","$APP_HOST","--port","$APP_PORT" ]