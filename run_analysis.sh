#!/bin/bash

for file in data/*.fastq.gz
do
    echo "Processing $file"
    python3 fastq_stats_gz.py $file
done
