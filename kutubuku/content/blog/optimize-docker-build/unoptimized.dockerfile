FROM python:3.12

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN pip install numpy

COPY matrixops.py .

ENTRYPOINT [ "python", "matrixops.py" ]
CMD ["--help"]