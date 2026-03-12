#!/bin/bash

INPUT_DIR="data"
OUTPUT_DIR="qc_results"
THREADS=4

mkdir -p $OUTPUT_DIR

echo "FastQC analysis started..."

for file in $INPUT_DIR/*.fastq.gz
do
    echo "Processing: $file"
    fastqc $file --threads $THREADS --outdir $OUTPUT_DIR
done

echo "FastQC analysis completed."
