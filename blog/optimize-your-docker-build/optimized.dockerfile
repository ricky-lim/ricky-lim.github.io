# Build stage
FROM python:3.12 AS builder

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --prefix=/install numpy

# Final stage
FROM python:3.12-slim

WORKDIR /app
COPY --from=builder /install /usr/local

COPY matrixops.py .

ENTRYPOINT [ "python", "matrixops.py" ]
CMD ["--help"]
