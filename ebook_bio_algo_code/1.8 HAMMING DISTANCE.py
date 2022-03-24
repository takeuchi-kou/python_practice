def hammingDist(t1,t2):
    hamDist = 0
    for i in range(0,len(t1)):
        if t1[i] != t2[i]:
            hamDist += 1
    return hamDist

t1 = 'AAAATCGCACCGGTTGGGGACAAAGGCGTTTAAACCTGCGAGCCCTCATTATTGAGGGTTGAGGAAGCAGGTCCACCGCATTCCCTGATAATAGAGCGCGAGACGAGGGTTTAACACCTGGAACCTCAATTCTGCACTTCCCCGTGTGGTGGGCTTGTGTCCCTGCGGGTCTACGCGTTAATTCAGGACGCAAGGGGCGGATGTAAACACTACAGTCTACTTCTGGGCACGCGCTTGTGCCTCACCTTGGCGATAAGATGGCTCCGGATGGTTCACGATGGCCTGAGCTCTTCAGGTCCGGTTAGACTCTTTGAAAATGAAGACTGGATCGACCTGAGCACCAGCAGCAGAATACTAACCCTCCATAGCTCACACTGTCTTTCCCCACGCGCATAACCGTTCCACTCCCCCCGGAGAGACGTTTTAAAAGTGGCTAGCAGGTTTAATGGGCACTTTTAAATAATTGAGTCCCCATGGCAAGTTTAGAACGGTAGGACAGATCCATTTTTGTCAAAGGGCCAGGTTTCGTCAATGATGCAGGACACGTTCTGAATCTCATCTCCTGCTAAATAACTACTTGGTGGCCGCGCAGGGACCATAACGATTTGTGACCAAGGCTTCGGTTGAGGTCTCTATAACTTTTCTGACCACTCTGACGCGAGGCATATAGGGCGCTGCGCCAAGCTTGATCGAGTCATGTTCATTTTTAGGCGCAGAATTAACCGGGAACTAGATACCCCAGGGTCCATAAAAACCTGTGCGTAGCCCTGGGTAATCTCTCCTGTGGGTCCCCGCCGCGTAAATTTTGTGCGCCAATTCGGCGCGTTTAACACCCGGTGGACCAGTGCTAGGCCCGATATTTACAGAGCAGGATTGGGGGTATTTACTCACCCTGGTGTCCCGCACAGACGACGTGTACCATGGAAAATTTGCTGATACCAGGTGCTCAGCCACTAGCAGTTAATTCTGGTAGCATATCAGGGATTGAGCCTATTCCACACTAACAACCCCTACTGTCGTGGCATACTAGGGCCTTAAGTCCGCACCTGAGAAGCCTCCTCCGGCCAAAGAGCA'
t2 = 'TTAGGTGTCACGCCCCCTTGGCAGTCTCTATAGCGAGATTTATAGAGACACGGTGCCTCCGCTGCGGGCATGAACCGAAATTCTCGCCCTCGACACTGTCGTCGACGTTCACCTCGCCTGGGTGCGTCAAGACTCGAACAAGTTCATGCCCGACCATTCGCGAAAAAGAGCTGCTCGCTTGGTAAGGTGGAGTAGCTGGTTCGCATACAAGCCGTAGCCAAATTCTGGTGAGTTTCAGTGTAACATGAGAGTACCTTGAGCACTGTCGACTCAGCCCGTCGCTCGTATGCTATGGAATAAAGGGCATCAGCTCGGCCTCCCTCAAGTTGCACAAGTTAGGGATGACTTGGGCCAGCTCTATGGCCGCATATGGCGGGGGGCCAGCTTTGGTCTAAGTTATGCCAATCGACGCGCTCAGTCGCGGTAGGTTACCCGCACGAAATATTGGGGCGTATGGCGCCCCTGACCGCGATACCGCCCAAAATGTCTTAGTTCTTAGCTGCTAGTAATTTACCTATCGGAAAATCGTGCTGCTACCCGGTTTCTTTGTTTCCATACGTGACACTACCACGTGCTCGCAAGGCTCTAAAGGAAGGGTTATGGTGATTCATCTAGGGCTTACCCATGCAATGCAACCGCTTCACCGGTTTCTAGCTAAGACCGACGGCCACACACCGACCGCGGAGTTTCCTCAGCAGCCCAGCGCGATCGGACATGAATGCCAACTTAGGAAGAGATGTCGCTGCAGGTGGACTCCGGGTCAATAAGAGGATTCACCAATAGGTATGCGTTCTACCGGATCTCGGCAACGCTATCGGGACCCGTGATCCGAATCTGGGTGTCAAATTCATATCGAGTTGGGCAGTCTTCACCTACCCATCTTCGCGTTGCCCTTAGAAGCCCAACGTACGGAGGACTCACTCCGTGACACATGCTGCAATCTGAAACTGCACCGGGTTCTTGTATTCGTAGTGGAAGGATCGCGCGGGCTATAGGCATTGCAAAAGCCTGATTACAGGGCGCTCGTCCCACTAATTATAGTCGGGTCCTAGCACGAATGGGCCCGCTCCGACG'
print(hammingDist(t1,t2))