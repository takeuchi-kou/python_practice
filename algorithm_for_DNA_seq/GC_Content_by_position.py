
import matplotlib.pyplot as plt


def readFastq(filename):
    sequences = []
    qualities = []
    with open(filename) as fh:
        while True:
            fh.readline()
            seq = fh.readline().rstrip()
            fh.readline()
            qual = fh.readline().rstrip()
            if len(seq) == 0:
                break
            sequences.append(seq)
            qualities.append(qual)
    return sequences, qualities

seqs, quals = readFastq('SRR835775_1.first1000.fastq')

def findGCByPos(reads):
    gc = [0] * 100
    totals = [0] * 100

    for read in reads:
        for i in range(len(read)):
            if read[i] == 'C' or read[i] == 'G':
                gc[i] += 1
            totals[i] += 1

    for i in range(len(gc)):
        if totals[i] >0:
            gc[i] /= float(totals[i])
    return gc

gc = findGCByPos(seqs)
print(gc)
plt.plot(range(len(gc)),gc)
plt.show()

import collections
count = collections.Counter()

for seq in seqs:
    count.update(seq)
print(count)