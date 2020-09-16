FROM python:alpine3.7

LABEL app="QIoT project"
LABEL maintener="David AUFFRAY <david.auffray@axians.com>"
LABEL major_version="1"
LABEL minor_version="0"

WORKDIR /usr/src/app

COPY requirements.txt ./

ENV FLASK_APP = /usr/src/app/app.py
ENV FLASK_APP_PORT = 8000
ENV FLASK_APP_HOST = 0.0.0.0
ENV FLASK_APP_DEBUG = "False"

RUN apk update && apk upgrade
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "app.py" ]