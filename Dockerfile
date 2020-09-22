    FROM python:3.8-alpine

    LABEL app="QIoT project - alpine version"
    LABEL maintener="David AUFFRAY <david.auffray@axians.com>"
    LABEL major_version="1"
    LABEL minor_version="0"

    WORKDIR /usr/src/app

    COPY requirements.txt ./

    ENV FLASK_APP /usr/src/app/app.py
    ENV FLASK_APP_PORT 8000
    ENV FLASK_APP_HOST "0.0.0.0"
    ENV FLASK_APP_LOG "--access-logfile"
    ENV FLASK_APP_LOG_FILE "/var/log/gunicorn.log"
    ENV GUNICORN_CMD_ARGS "--bind=$FLASK_APP_HOST:$FLASK_APP_PORT $FLASK_APP_LOG $FLASK_APP_LOG_FILE"

    RUN apk add gcc libc-dev make linux-headers libgpiod-dev i2c-tools git
    RUN pip install --no-cache-dir -r requirements.txt
    # RUN git clone https://github.com/pimoroni/enviroplus-python.git /enviroplus

    COPY . .

    CMD [ "sh" ]
