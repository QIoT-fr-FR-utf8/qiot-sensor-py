FROM quay.io/acb-fr/qiot-sensor-service-base:1-aarch64
RUN dnf update
RUN dnf install make -y
RUN pip3 install --no-cache-dir -r requirements.txt
