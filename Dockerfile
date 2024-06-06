FROM ubuntu:22.04
LABEL desc="-_-"
RUN apt update && apt install software-properties-common -y && add-apt-repository ppa:deadsnakes/ppa && apt update
RUN apt install python3.10 -y python3.10-venv -y python3.10-dev -y && apt-get install git -y
RUN apt install python3-pip -y && pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu \
 && pip install --upgrade setuptools
RUN mkdir -p /app && mkdir -p /app/output && mkdir -p app/test/actual
WORKDIR /app
COPY ./../requirements.txt /app/
RUN pip install -r requirements.txt
COPY ../run.py /app/
ADD ../tsr /app/tsr
ADD ../test /app/test
ADD ../image_to_compute /app/image_to_compute
COPY ./createImagePath.sh /app/

CMD [ "ls" ]