def ptmatch(p, t):
    position = []
    for i in range(0, len(t) - len(p) + 1):
        if t[i : i + len(p)] == p:
            position.append(i)
    j = ''
    for i in position:
        j = j + str(i) + ' '
    return j

p = 'CTTGATCAT'
t = 'GCCCGCCTCAACCAACGCCTCACTGCGCCTCACGCCTCAACTACGCCTCACCGTCACGCGCCTCACACGCCTCAACCCGCCTCAGTGTCACGCCTCACGCCGCCTCAACGCCTCACGCCTCAGGCGCCTCAAATCGCCTCACGCCTCACGCCTCATTGTCGCCTCACCCCCTGTGGCGCCTCACTCGCCTCAACCGCCTCACGCCTCAACGCCTCATCCGCCTCAACGCCTCACGCCTCATAAACCGCCTCACACGGTACGCCTCAGGCCGAAGACCCGCCGCCTCAGCGCCTCATGACGCCTCATAACGCCTCATCGCCTCACGCCTCAACGACCGTTCGCCTCACGCCTCAGTCCGCCTCACGCCTCATCCGCCTCAGACGCCTCATTCCTGCGCCTCACCGCCTCAACGCCTCATAACCGTCGCCTCACGCCTCACGCCTCAGGCCGCGCGCGCGCCTCAACGCCTCACGCGTGACGCCTCACGCCTCATTGTAGCCCGCCTCATAGTAGCGCCTCACCCGCCTCACAGTACTCTCTCGCCTCAGAGACGCCTCAGCGCCTCAAGGTGCGCCTCATTACGCCTCACTGGACGGCCGCCTCAGCGCCTCACGCCTCACGGCGCCTCACGCCTCACACCGCCTCAAACGCCTCATCTACCGCCTCACCCGCCTCACCCGCCTCAGGATGTTGCTCGAGCTCGCCTCACGCCTCAATAGCGCCTCACCGCCTCATCTTCCGCCTCAGAGCGCGCCTCACGCCTCAGCGCCTCACGCCTCACGCCTCAACCGCCTCACGCCTCACCCGCCTCACGCCTCACATTCGAGCGCCTCATCTTAAGACCGCCTCACGCCTCATCGCCTCAAGTCGCCTCAATCACGCCTCAACGCCTCACTTAGGCGCCTCACCCTATTTCGCCTCACTCGCCTCACGCCTCACGCCTCATCGCCTCAACGCCTCACGCCTCAGGGTCAGCGCCTCACGCCTCACGCCTCACCAACACGCCTCACGCCTCAATCGCCTCAATACGCCTCAGATCGCCTCATTCCGCCTCATTTTGCGCCTCAACGCCTCATGACGCCTCAGATCGCCTCAAGCGCCTCACCTCGCCTCAACGCCTCAGATTCGCCTCACTCCGCCTCACGCCAATAGCGCCTCACCGCCTCACCATAACGCCTCAGACGCCTCATCCCCGCCTCACGCGCCTCACCCCGCCTCACGCCTCAGGCGCCTCAGCGAGTACGCGCGCCTCATTAACGCCTCAACGCCTCATCCGCCTCACAATGAGGGCCGCCTCAGCATATTGTTACGCGCGCCTCACGCCTCACGCCTCACGCCTCAGCCCCGCCTCACCGCCTCAAAAACGCCTCAAACGACGCCTCAGTACGCCTCATTCGCCTCAAGGTGCGCCTCACGCCTCACAGCGCCTCAGCTCGCCTCATCGCCTCACGCCTCAGTTTTCGCGCCTCACGCCTCAGCGAAATCGCCTCAAGAGACTGGGGGCGCCTCACCGCCTCAGCCAACGCCTCAACACGCCTCACGCCTCACGCCTCACGCCTCAATCGCCTCAACCCCGCCTCACCGCCTCACGCCTCATATCGCCTCAACTAGCCTCGCCTCATTTGCTCGCGCCTCACGCCTCACGGGCGCCTCAACGCCTCAGTCACGCCTCAGACCCGCCTCAAGATCGCCTCACGCCTCACCGCCTCATGCGCCTCACAACGCCTCACGCCTCATCGCCTCACACCGCCTCATTCACGCCGCCTCACGCCTCAATAATCACGCCTCACTACGCCTCACCGCAATTATGTCGCCTCAGCGCCTCAGTCGCCTCACGCCTCACGCCTCAACGCCTCAACGCCTCACGCCTCACGCCTCAGAAACCGCCTCAACCCGCCTCAAGGCGCCTCAATGCGCCTCAAACGCCTCATCGCCTCAAATAAATACCCGCCTCACTCCGGTGGAAATCGCCTCACGCCTCAGTCGCCTCAGTCGCCTCATATACGCCTCACGCCTCACGCCTCACAGCGCCTCACCGCCTCAGATATGTTTTACAATCGCCTCATGCGCCTCATCCTACGCCTCACGCCTCACGCCTCACCCGCCTCACCGCCTCACGCCTCAACGCCTCACCTTCGCCGCCTCACGCCTCATCGCCTCATTCGCCTCACGCCTCAGCGCCTCAGGGGGTACCGCCTCACGCCTCAAGACGCCTCAAGCGCCTCATTCGCCTCATCGGATCGCCTCACTGGCTGGCCGCCTCATCGCCTCATGCGCCTCATCCGCCTCACGCCTCAGCGCCTCATCACCCCACGCCTCACGCCTCAGCTATACGCCTCAACGACGGTAGCGCCTCAACGCCTCAGCTTAGGACGCCTCACGCCTCAGTTGACGCCTCAGCCATATCGCCTCACGCCTCACCGCCTCAGCGCCTCAAACGCGCCTCAGACGCCTCAGCCCCCCGCCTCAACGCCTCAAAATCATCGCCTCAGCATAGCGCCTCATGGCGCCTCATGCTCGCCTCACTCGCCTCATCGCCTCATGACGCCTCAAGACGCCTCACGCCTCACGCCTCAGTAACGCCTCAATCGCCTCACCGCCTCAAAGAGCGCCTCAATAAAGCGCCTCACACGCCTCACGCCTCAACGCCTCACGCCTCAATTTAGGCGCCTCAGGCGCCTCAGTCTTTTCGCCTCATCGCCTCAAACGCCTCATCCGCCTCATACGCCTCATCCGAGCACGCGCTCTCCCTGAGGTCGGTCGCCTCAAGCGCCTCACCGCCTCACGCCTCACGATTGCGCCTCAACGCCTCATCCGCCTCACGCCTCAGTCGCCTCACGCCTCACATTTCGCCTCATCCGCCTCAGCGCCTCACCTCGCCTCAAGCGCGCCTCACGCCTCAAATCGCCTCAGCAACGCCTCACGCCTCACGCCTCACAGCGCCTCACAGCGCCTCACGCCTCAGCGCCTCAAACCACCGCCTCACGCCTCACGCCTCACGCCTCACTGATCGCCTCACTATCGCCTCACCGCCTCACTCGCCTCAGCGCCTCATCGCCTCATATTCGCCTCACGCCTCAGGAAACGCCTCATAATTGCGCGCCTCAGACGCCTCACAATTAGGGGACGCCTCAGCGCCTCAAGTACGCCTCACGCCTCATCTTCCCCCGGTCGCCTCATCTCGCCACGGGCGCCTCATCCGCCTCAACGCCTCACCGCCTCATCGCCTCAAACGCCTCACGCCTCAACAACGCCTCACTCGCCTCATCTGCCGCCTCACTGGCGCCTCACGCCTCATCGCCTCATCGCCTCACTCGCCTCACGCCTCAGATCGCCTCAGCGCCTCACGCCTCATGGGGCCAGGACGCCTCACGCGCCTCATCGCCTCACAGTACCCGCCTCAAGTACGCCTCACATCGCCTCATGAGTTCTCGCCATTTCGAAGCCGCCTCAACGCCTCATCACGCCTCATCGCCTCAGTTGATTTTCGCCTCACTGCGCCTCACGCCTCAGGGCCCACGCCTCAACATCCGCCTCACAGCCGCCTCATCTGACGCCTCACCGCCTCACGCCTCACGCCTCACGCCTCAAAAACGCCTCAGCGCCTCACAGGGGACGTGCCAGCTCGCCTCACGCACCGCCTCATAAACGCCTCACGCCTCAGCGCCTCAGCGCCTCAGCGCCTCAGCGCCTCAGCGCCTCATGAGAAAGTTCGCCTCATACGCCTCACGCCTCACCGCCTCACGCCTCAAGCCATCGCCTCATCGCGCCTCAAATTATGCCGCCTCACTTGCGCCTCAGAACGCCTCACCGCCTCAGCGCCTCAGCTAAATGGCGCCTCACGCCTCAACGCCTCATCGGGCGCCTCATCTTACGCCTCACCGCCTCAGACGCCTCACGCCTCAGGCGTACGCCTCAACCCCGCCTCAAACGCCTCATCGCCTCATCTGGACGCCTCATGCGCCTCAACGTCCGCCTCACGCCTCAGGGCGCCTCACGCCTCATCGCCTCACGCCTCACGCCTCACGCCTCATGGCGTAGCATCTACGTGCGCCTCAAGACCGCCTCACGCCTCACGCCTCACGGCGCCTCATCGCCTCAGCCGTGTAGGCCCGCGCCTCATTTCGCCTCATCTCGCCTCAGCCCGCCTCACTCTCGCCTCACGCCTCACGCCTCATTGAAGCGCCTCAGTGGTGTCGCCTCACGCCTCACGCCTCATCAGACGTACCGCCTCATGGTGGGCGCAAGGAACGCCTCACGTCGCCTCAGTCGCCTCATATGTAACGCCTCAACGCCTCAACAATCGCCTCACTAAAGAAACGCCTCAGCGCCTCACGAAGGAATCGCCTCACACGCCTCAAAAACGCCGCCTCAAATCGCCTCACCGATGTCGCCTCAATGAGGCCGCCTCACCGCCTCAGCGCCGCCTCAGCATACGCCTCATGTGCTCGCCTCACACCGCCTCAACCTCGCCTCAGTCGCCTCAGCGCCTCACGCCTCACGCCTCAGTGATCGCCTCAAATAACGCCTCACGCCTCAACGCCTCACGAGGCGCCTCAATCTCACTCGCCTCAGTCGCCTCAATTCGCCTCAGCGCCTCATCGCCTCACGCCTCACGCCTCAGTCGCCTCAACGCCTCAAGCGCCTCAATACGCCTCAAAGCGCCTCATCCGCCTCACCGCCTCACTGCGGATTCGCCTCAACGCCTCAGCCGCCTCAAGCGCCTCACGCCTCACGCCTCAAACTAGCACCGCCTCAGGCCGCCTCACGCCTCACGCCTCACGCCTCAACATGACGCCGCCTCATCCGTTCGCCTCAGATACGCCTCAACTTAGTTGCGCCTCACGCCTCAACGCCTCACGCCTCACGCCTCAACGCCTCATCGCCTCAACAACCGCCTCAGAAAAACCGCCTCACCGCCTCATGAAACGCCTCACAACACGTTTTATATCGCCTCATCACGCCTCACCGCCTCACGCCTCACCGCCTCAGCGCCTCAGACAGCGCCTCAGTCGCCTCATTTCAACGCCTCATCCCCCCGCCTCATCGCCTCACAGTCGCCTCACCGCCTCATGACGCCTCAGTATTTACGCCTCAGCGCCTCACAGAGCCGCCTCATCGCCTCACGCTGACCCGACCCTCGTTTGCTTCGCCTCAACGCCTCAGGCGCCTCAATCAACGCCTCAGTTGGCAACTGACGCCTCACGCGCGCCTCAGCGCCTCATCGCCTCAAGCGCCTCACGCCTCATCTGGGCGCCTCAGCCGCCTCACGCCTCACGCCTCACGCCTCACGCCTCACGCCTCAGCGCCTCAATAACGCCTCAGCGCCTCATGAGGGCGCCTCACCGCCTCACGCCTCAGACGCCTCAGCGCCTCATGGAACTAATTCGCCTCACGCCTCAAACGCCTCAGTCTCCGCCTCAAGCGCCACTCCGCCTCACGCCTCATCGGTCTTGACGCCTCACGCCTCACGCCTCACAATCGCCTCGCCTCACCGCCTCACCTTCACCGCCTCACGCCTCACGCCTCACGCCTCACGCCTCAGACGCCTCAAATCCGCCTCACGCCTCAACGCGCCTCAATCACGCCTCACACCGCCTCACGCCTCATACCGCCTCAGGCGCCTCACGCCTCAGCCGCCTCACCCGCCTCAGCGCCTCAGCGCCTCAACGCTCGCCTCATTCCGCCTCACCGCCTCAATAGTAGCGCCTCACCGCCTCACGCCTCACCGCGTATTCCGCCTCAGGTAATATTATCCGCCTCATGTAGTTCTCAACAACGCCTCACGCCTCACGCCTCAACGCCTCAATCAGTCGCCTCACGCCTCACCGCCTCAGACGCCTCACGCCTCAGTTCGCCTCAACGCCTCATGTCGCCTCAGCGCCTCAGTCGCCTCACGCCTCAGGGACCCGCCTCAAACGCCTCACGCCTCACCGCCTCACGCCTCATTCGCCTCACGCCTCACGTCGCCTCACTGCGCCTCAAACCGCCTCACCGCCTCAATCCGCCTCAACGCCTCACGCCTCAACCAACGACGCCTCACCCCGCCTCAGCTAACCTTGGGTGGTCGCGCCTCAAGATAACGAACGCCTCATCGCCTCACACGCCTCACCGCCTCACGCCTCACGCCTCACGTTACGACGCCTCACGCCTCACCCGCCTCACCGCCTCAAAACGCGCCTCAGACTACGCCTCATCCGCCTCACCGCCTCATCCGCCTCACAGTGCGTCGGACGCCTCATGCACGCCTCACCGCCTCACGCCTCAGTCGCCTCAACATGGGCCGCGCCTCATTCCCGCCTCAACGCCTCACGCCTCATCGCCTCATGCTCATCGCCTCACGCCTCAATCCGCCCGCCTCAGCATTTTCGCCTCACGCCTCACGCCTCAGCGAGCACCGCCTCATTGCGCCTCAACATTGGCGCCTCACGCCTCACGCGCCTCATCGCCTCATCGGCGCCTCACGCCTCAGCGCCTCATCGCCTCAACGCCTCACTACGCCTCAGATACATCCTCGCTCGCCTCATGCCGCCTCATTAGCGCCTCACCGCCTCACTTACGCCTCAGCGCCTCAACGTCGTAGCCGCCTCATGGACGCCTCACGCCTCAGTTACAGCCGCCTCACGCGCCTCATGGCCGCCTCACGCCTCATTCGCCTCAACGCCTCACGCCTCATGCGCCTCAGCGCCTCAAAGTATCGCCTCAAGCGACGCCTCACCTCCCGCCTCACCGCCTCACCCCGCCTCAACGCCTCACCGCCTCACGCCACGCCTCATGGCGCCTCATCGCCTCACTGGGCCTGCGCCTCAGTTACGCCTCACGCCTCAACGCCTCACTCGCGCCTCAGGGCCGCCTCACCGCCTCACGCCTCACGGCCTTCGCCTCATCGCCTCAACTTCGGTCGCCTCATTCGCCTCACGCCTCAACTCCGCCTCAAGTTCGTACAACGCCTCATAAATTATAGACAGCGCCGCCTCACGCCTCAGCGCCTCAGGCCGCCTCAGACGCCTCATCTGGCGCCTCAGCGCCTCACATTGGGTAACGCCTCAGAGATACGCGCCTCACGCCTCACGCCTCAGCGCCTCATCCACGCCTCAGACGCCTCAACTTCGCCTCAACTATCGCCTCATTAACCACACGCCTCAACGCCTCAGACGCCTCAAGCGCCTCAGATCGCCTCAACACGCCTCACGCCTCAGACGCCTCAAAGGACCCGCCTCACGCCTCAGTCTACGCCTCAGTGGTGTCCGCCTCACCGCCTCAACGCCTCAGCGCCTCACGCCTCAAAAACGCCTCACGCTTCACGTCGCCTCAACGCCTCAAGCGCGCCTCAAGACGTAGTTGATCCCGCCTCACGCCTCAATACGCGCCTCAACTCCGCCTCATCAGGCTGCGCCTCACGCCTCACGCCTCAAGGATCCGCCTCACGCCTCATATCCGCCTCACGCCTCAGGCGCCTCAAACCGCCTCACGTCGCCTCATGTACGCCTCAACTGTCTCGCCTCAATCCCCCGCCTCACGCCTCACGCCTCAACCCTGCGCCTCACGCCTCAGTCGCCTCACGCCTCAAGCGCCTCAGCCGCCTCACTGCGCCTCACGCCTCATCGCCTCACGCCTCAAGTCTGCGCCTCACATCGCGCCTCACGCGCCTCATCACGCCTCAGATCTAGCGCCTCAGACGCCTCAGCCAAAGCGCCTCAGTTTCGCCTCAGCGCCTCAAGTCGCCTCACCGAAAAAACGCCTCACTCGCCTCATTAACGCCTCACGCCTCAGCGCCCGCCTCATCATCGCCTCACGAACGAACGCCTCAACGCCTCAATCCGCCTCACAACGCCTCATACCGCCTCACGACTACGCCTCATACGCCTCAGGGATGCAGGGCGCCTCACGCCTCATGTTCGCCTCATCCAAAGCGCCTCACGCCTCACGCCTCACTTCCGCCTCACACCGCCTCAATCCGCCTCACCTGTTCACGCCTCACCGCCTCAGCGCCTCATTACGCCTCACGCCTCACGCCTCACGCCTCACGCCTCAGTGGTTTACGCCTCATCGCCTCACTGTCGCTCAACGCCTCACCGCCTCATGACGCCTCAAATACGCCTCACGCCTCACGCCTCATATCGCCTCATCGCCTCAACGCCTCAAATCCATCGCCTCACAACGCCTCACGCCTCAAGGCGCCTCAGATCCGCCTCAAAGGTCACGCCTCATCGGGCGCCTCACATAAATCACGCCTCACCGCCTCAAGCCTCCGACCCGCCTCACGCCTCATTGCCGCCTCACGCCTCAAGGTACGCCTCACGCCTCACCGCCTCACGCCTCACGCCTCAGCCGCCTCACGCCTCAAGTTTCGCGCCGCCTCATGCCGCCTCACGCCTCATGCGCCTCAGAGGGCGCCTCACGCACGCCTCAGGACGCCTCAGCGCCTCATAGCGATAAGTCCGCCTCAACATCGCGCCTCAACGCCTCAAGCCGCCTCACGCGCCTCAAACGCCTCAACCGCCTCACGCCTCATCCGCCTCAGCTAAACGCCTCACTCGCCTCACGCCTCATCGCCTCAGCGCCTCATGCGCCTCACGCCTCAGAGCACGCCTCAAACTCGCCTCAGCGCCTCATTTTCGCCTCAGAACGCCTCACCGCCTCACGCCTCAACGCCTCAGCGCCTCACGCCTCAAAAGGTTCGCCTCAACTGGGACGCCTCACGCCTCAACCGCCTCACGCCTCACACGCCTCACGCCTCATGATCGCCTCACGCCTCACGCCTCACGCCTCAGCCGCCTCACGCCATCCCGCCTCACGCCTCACGCCTCACGCCTCATTCGCCTCAGCGCCTCAGCTCCGAGAGTTGACGCCTCACGCCTCAAGACCGCCTCACGCCTCACTCCGCCTCAAGGTTCTCGCCTCAAGCGCCTCAGCGCCTCACGCCTCATCGAACGCCTCACGCCTCACGCCTCACGCCTCATCGCCTCATCCTCGAGGCTTGGAGCGCCTCACGGTTGCGCCTCAGTCAGCGTCGCCACACGCCTCAATGGCGCCTCACACTCGCCTCACTGTCGCCTCATCGCCTCATAAATCAGTACGCCTCAGCGCCTCATCGCCTCAAACGCGCCTCAATCGCCTCACGCCTCACGCCTCAACGCCTCACGCCTCACGCCTCACGCCTCACGCCTCAAATATAGCGCCTACGCCTCAACGCCTCACGCCTCACTAGATCGCCTCAGCGGCGCCTCAACGGGCGCCTCACGCCTCAAAACATCGCCTCAGGATTATACCGCCTCAAGTTCGGTCGCCTCACCGCCTCACCGCCTCAAAGTCGCCTCA'
print(ptmatch(p,t))