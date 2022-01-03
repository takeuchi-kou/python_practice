alphabet = {'A', 'C', 'G', 'T'}
score = [[0,4,2,4,8],\
         [4,0,4,2,8],\
         [2,4,0,4,8],\
         [4,2,4,0,8],\
         [8,8,8,8,8]]

def globalAlignment(x,y):
    D = []
    for i in range(len(x)+1):
        D.append([0]* (len(y)+1))

    for i in range(len(x)+1):
        D[i][0] = D[i-1][0] + score[alphabet.index([i-1])][-1]
    for i in range(len(y)+1):
        D[0][i] = D[0][i-1] + score[-1][alphabet.index(y[i-1])][-1]

    for i in range(1, len(x)+1):
        for j in range(1,len(y)+1):
            disHor = D[i][j-1] +1
            disVer = D[i-1][j] +1
            if x[i-1] == y[j-1]:
                disDiag = D[i-1][j-1]
            else:
                disDiag = D[i-1][j-1] +1

            D[i][j] = min(disVer,disHor,disDiag)

    return D[-1][-1]
