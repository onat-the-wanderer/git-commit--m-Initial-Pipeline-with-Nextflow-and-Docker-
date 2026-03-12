#!/usr/bin/env python3

import gzip
import sys
import numpy as np
import matplotlib.pyplot as plt

fastq = sys.argv[1]
prefix = sys.argv[2]

gc_vals = []
len_vals = []
qual_vals = []

def gc_content(seq):
    gc = seq.count('G') + seq.count('C')
    return (gc/len(seq))*100

def mean_q(qual):
    return np.mean([ord(c)-33 for c in qual])

with gzip.open(fastq,"rt") as f:

    while True:
        h = f.readline().strip()
        if not h:
            break

        seq = f.readline().strip()
        f.readline()
        qual = f.readline().strip()

        gc_vals.append(gc_content(seq))
        len_vals.append(len(seq))
        qual_vals.append(mean_q(qual))

gc_vals = np.array(gc_vals)
len_vals = np.array(len_vals)
qual_vals = np.array(qual_vals)

# summary stats
with open(prefix+"_summary.txt","w") as out:

    out.write("GC Content\n")
    out.write(f"Mean\t{np.mean(gc_vals)}\n")
    out.write(f"Median\t{np.median(gc_vals)}\n\n")

    out.write("Read Length\n")
    out.write(f"Mean\t{np.mean(len_vals)}\n")
    out.write(f"Median\t{np.median(len_vals)}\n\n")

    out.write("Mean Quality\n")
    out.write(f"Mean\t{np.mean(qual_vals)}\n")
    out.write(f"Median\t{np.median(qual_vals)}\n")

# GC plot
plt.hist(gc_vals, bins=30)
plt.title("GC Content Distribution")
plt.xlabel("GC %")
plt.ylabel("Frequency")
plt.savefig(prefix+"_gc.png")
plt.clf()

# length plot
plt.hist(len_vals, bins=30)
plt.title("Read Length Distribution")
plt.xlabel("Length")
plt.ylabel("Frequency")
plt.savefig(prefix+"_length.png")
plt.clf()

# quality plot
plt.hist(qual_vals, bins=30)
plt.title("Mean Quality Distribution")
plt.xlabel("Mean Quality")
plt.ylabel("Frequency")
plt.savefig(prefix+"_quality.png")