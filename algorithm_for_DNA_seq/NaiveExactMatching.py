# read genome
def readGenome(filename):
    genome = ''
    with open(filename, 'r') as f:
        for line in f:
            # ignore header line with genome information
            if not line[0] == '>':
                genome += line.strip()
    return genome

genome = readGenome('phix.fa')

# match exactly
def naive(p, t):
    occurrence = []
    for i in range(len(t) - len(p) + 1):
        match = True
        for j in range(len(p)):
            if not t[i + j] == p[j]:
                match = False
                break
        if match:
            occurrence.append(i)
    return occurrence


t = 'AACGTACGATTACG'
p = 'AC'
print(naive(p, t))
print(t[1:3])

# generate artificial string
import random
def generateReads(genome, numReads, readLen):
    '''Generate reads from random positions in the given genome.'''

    reads = []
    for _ in range(numReads):
        start = random.randint(0, len(genome) - readLen) - 1
        reads.append(genome[start : start + readLen])
    return reads
reads = generateReads(genome, 100, 100)

# match artificial strings to original sequence
numMathed = 0
for r in reads:
    matches = naive(r, genome)
    if len(matches) > 0:
        numMathed += 1
print('%d / %d reads matched exactly!' % (numMathed, len(reads)))

# read real sequence from fq file
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

phix_reads, _  =  readFastq('ERR266411_1.first1000.fastq')

# match reads to fq genome
numMathed = 0
n = 0
for r in phix_reads:
    r = r[:30]
    matches = naive(r, genome)
    n += 1
    if len(matches) > 0:
        numMathed += 1
print('%d / %d reads matches the genome!' % (numMathed, n))

# the match rate is low because there are a pair of sequence but only a single string
# so we're gonna make a reverse complement string
def reverseComplement(s):
    complement = {'A':'T',"T":'A','G':'C','C':'G','N':'N'}
    t = ''
    for base in s:
        t = complement[base] + t
    return t
numMathed = 0
n = 0
for r in phix_reads:
    r = r[:30]
    matches = naive(r, genome)
    matches.extend(naive(reverseComplement(r), genome))
    n += 1
    if len(matches) > 0:
        numMathed += 1
print('%d / %d reads matches the genome!' % (numMathed, n))