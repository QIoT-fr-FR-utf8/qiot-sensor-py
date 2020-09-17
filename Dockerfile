FROM fedora:31
RUN dnf update
RUN dnf install make -y
RUN pip3 install --no-cache-dir -r requirements.txt
