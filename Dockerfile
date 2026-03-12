FROM python:3.10-slim

RUN apt-get update && apt-get install -y \
    fastqc \
    default-jre \
    && rm -rf /var/lib/apt/lists/*

RUN pip install numpy matplotlib

WORKDIR /pipeline

COPY fastq_stats_gz.py .
