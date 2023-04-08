FROM python:3.10-slim-bullseye

WORKDIR /app

COPY requirements.txt .
RUN apt-get update && apt-get upgrade && apt-get -y install curl build-essential && curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y && pip3 install -r requirements.txt && apt remove -y curl build-essential && apt -y autoremove
ENV PATH="$PATH:/root/.cargo/bin"

COPY requirements.txt .
RUN pip3 install -r requirements.txt

ARG MODEL_NAME
ARG ONNX_RUNTIME
ARG ONNX_CPU
COPY download.py .
RUN ./download.py

COPY . .

ENTRYPOINT ["/bin/sh", "-c"]
CMD ["uvicorn app:app --host 0.0.0.0 --port 8080"]
