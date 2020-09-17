FROM fedora:31
RUN dnf -y update
RUN dnf -y install libgpiod-utils i2c-tools libi2c-devel gcc python3-devel python3-pip
RUN pip3 install enviroplus
RUN dnf -y install python3-numpy python3-i2c-tools python3-pillow python3-setuptools python3-libgpiod python3-libgpiod python3-RPi.GPIO
RUN dnf -y install python3-cffi
RUN python3 -m pip install sounddevice
RUN dnf -y install portaudio

WORKDIR /usr/src/app

COPY requirements.txt ./

ENV FLASK_APP /usr/src/app/app.py
ENV APP_PORT 8000
ENV APP_HOST "0.0.0.0"
ENV APP_DEBUG "False"

<<<<<<< HEAD
=======
RUN dnf install -f make
RUN pip install --no-cache-dir -r requirements.txt
>>>>>>> parent of c3b9561... correct Dockerfile

RUN sudo dnf install make -y
RUN pip3 install -r requirements.txt

RUN dnf clean all
COPY . .

CMD [ "uvicorn", "app:app","--host","$APP_HOST","--port","$APP_PORT" ]