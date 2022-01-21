def hammingDist(t1,t2):
    hamDist = 0
    for i in range(0,len(t1)):
        if t1[i] != t2[i]:
            hamDist += 1
    return hamDist

def ApproximatePatternCount(t, p, d):
    count = 0
    for i in range(0,len(t)-len(p)+1):
        p_alt = t[i:i+len(p)]
        if  hammingDist(p,p_alt) <= d:
            count += 1
    return count

p = 'CGCTGA'
t = 'CCGCTCTAGAAACCTTGCAATTGAGGGTACACCGTCTATAATGATGCCTAAGCCTTGGTTAGCCACTCCAGGTCTCAGCACGCGACAAGTTTGCCGCAACCGAACGCTTACAAGTTGCGCTGAGCTTGCTGTGTGTGGTATTCACTTATATAACAATAATCTTATTCCGAATGGCACGTACTGGTGTTGTTGGAATCTCAATAACGTCCCCCCATTCCACAAACACCGACCAATCTGACGTTCACTCCTATTATGTGATGTCTCCGGCGGAGTTAGCAGTCGGTCGTGGGTCGCTACCAGAGATATTTTAAGCTTCAATGATTCTTGGTCACGAGGCCCCAATTT'
d = 3
print(ApproximatePatternCount(t,p,d))