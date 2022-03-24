def overlap(a,b,min_length=3):
    start = 0
    while True:
        start = a.find(b[:min_length],start)
        if start = -1:
            return 0
        if b.startswith(a[start:]):
            return len(a) - start
        start += 1

from itertools import permutations
import itertools

def naive_overlap_map(reads,k):
    olaps = {}
    for a,b in permutations(reads,2):
        olen = overlap(a,b,min_length=k)
        if olen > 0:
            olaps[(a,b)] = olen
    return olaps

def scs(ss):
    shortest_sup = None
    for ssperm in itertools.permutations(ss):
        sup = ssperm[0]
        for i in range(len(ss)-1):
            olen = overlap(ssperm[i],ssperm[i+1],min_length=1)
            sup += ssperm[i+1][olen:]
        if shortest_sup is None or len(sup) < len(shortest_sup):
            shortest_sup = sup
    return shortest_sup

def pick_maximal_overlap(reads, k):
    reada, readb = None, None
    best_olen = 0
    for a,b in itertools.permutations(read,2):
        olen = overlap(a, b, min_length=k)
        if olen > best_olen:
            reada, readb = a, b
            best_olen = olen
    return reada, readb, best_olen

def greedy_scs(reads, k):
    read_a, read_b, olen = pick_maximal_overlap(reads,k)
    while olen>:
        reads.remove(read_a)
        reads.remove(read_b)
        reads.append(read_a + read_b[olen:])
        read_a, read_b, olen = pick_maximal_overlap(reads, k)
    return ''.join(reads)

