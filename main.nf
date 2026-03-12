nextflow.enable.dsl=2

process FASTQC {

    tag "$fastq"

    input:
    path fastq

    output:
    path "*_fastqc.*"

    publishDir "results/fastqc", mode: 'copy'

    script:
    """
    fastqc $fastq
    """
}

process READ_STATS {

    tag "$fastq"

    input:
    path fastq

    output:
    path "*_summary.txt"
    path "*_gc.png"
    path "*_length.png"
    path "*_quality.png"

    publishDir "results/qc_stats", mode: 'copy'

    script:
    def sample = fastq.baseName

    """
    python3 ${projectDir}/fastq_stats_gz.py $fastq $sample
    """
}


workflow {

    reads = Channel.fromPath("data/*.fastq.gz")

    FASTQC(reads)
    READ_STATS(reads)

}