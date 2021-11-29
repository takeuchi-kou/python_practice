
def readFile(filePath):
    """Reading a file and returning a list of lines"""
    with open(filePath, 'r') as f:
        return [l.strip() for l in f.readlines()]

def gc_content(seq):
    """GC Content in a DNA/RNA sequence"""
    return format(((seq.count('C') + seq.count('G')) / len(seq) * 100), '.6f')

# Calculate GC Content from FASTA formatted text file:

# === Read data from the file (FASTA formatted file)
# Storing File contents in a list
FASTAFile = readFile("test_data/gc_content.txt")
print(FASTAFile)
# Dictionary for Labels + Data
FASTADict = {}
# String for holding the current label
FASTALabel = ""
# === Clean/Prepare the data (Format for ease of you with our gc_content function)
# Converting FASTA/List file data into a dictionary
for line in FASTAFile:
    if '>' in line:
        FASTALabel = line
        FASTADict[FASTALabel] = ""
    else:
        FASTADict[FASTALabel] += line
print(FASTADict)

# === Format the data (store the data in a convenient way)
# === Run needed operation on the data (pass the data to our gc_content function)
# Using dictionary comprehension to generate a new dictionary with GC content
RESULTDict = {key: gc_content(value) for (key, value) in FASTADict.items()}
print(RESULTDict)

# Looking for max value in values() of our new dictionary
MaxGCKey = max(RESULTDict, key=RESULTDict.get)
# === Collection results (Rosalind Submission in our case)
# Printing Rosalind formatted resulet
print(f'{MaxGCKey[1:]}\n{RESULTDict[MaxGCKey]}')