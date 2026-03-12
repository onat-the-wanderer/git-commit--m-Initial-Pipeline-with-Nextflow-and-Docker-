# FASTQ QC Nextflow Pipeline

This repository contains a simple bioinformatics pipeline for FASTQ quality control.

## What the pipeline does

The pipeline performs:

1. FastQC analysis
2. Custom read-level statistics calculation
3. Distribution plots for:
   - GC content
   - Read length
   - Mean read quality
4. Summary statistics output

## Project structure

```bash
fastqc_file/
├── main.nf
├── nextflow.config
├── environment.yml
├── README.md
├── scripts/
│   └── fastq_stats_gz.py
├── data/
│   └── example.fastq.gz
