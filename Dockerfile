FROM python:alpine3.7

WORKDIR /usr/src/app

COPY requirements.txt ./

ENV FLASK_APP = /usr/src/app/app.py
ENV FLASK_PORT = 8000
ENV FLASK_HOST = 0.0.0.0
ENV FLASK_DEBUG = "False"

RUN apk update && apk upgrade
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "app.py" ]
