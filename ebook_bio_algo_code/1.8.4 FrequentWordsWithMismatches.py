


def FrequentWordsWithMismatched(t,k,d):
    patterns = []
    freqMap = {}
    n = len(t)
    for i in range(0,n-k):
        p = t[i:i+k]
        neiborhood = Neibors(p,d)
        