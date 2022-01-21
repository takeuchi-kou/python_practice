def hammingDist(t1,t2):
    hamDist = 0
    for i in range(0,len(t1)):
        if t1[i] != t2[i]:
            hamDist += 1
    return hamDist

def Neighbors(p,d):
    if d == 0:
        return str(p)
    if len(p) == 1:
        return ['A','C','G','T']
    Neiborhood = []
    nucleos = ['A','C','G','T']
    suffixNeib = Neighbors(p[-len(p)+1:],d)
    for text in suffixNeib:
        if hammingDist(p[-len(text):],text) < d:
            for nuc in nucleos:
                Neiborhood.append(nuc + text)
                print(Neiborhood)
        else:
            Neiborhood.append(p[0] + text)
    return " ".join(Neiborhood)

p = 'ACG'
d = 1

print(Neighbors(p,d))
                