def PatternCount(t,p):
    count = 0
    for i in range(0,len(t)-len(p)+1):
        if t[i:i+len(p)] == p:
            count += 1
    return count

def FrequentWords(t, k):
    fpatterns = set()
    count = [0]*(len(t)-k+1)
    for i in range(0, len(t)-k):
        p = t[i:i+k]
        count[i] = PatternCount(t, p)
    MaxCount = max(count)
    for i in range(0, len(t)-k):
        if count[i] == MaxCount:
            fpatterns.add(t[i:i+k])
    return fpatterns
