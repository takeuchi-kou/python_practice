# DNA Toolset/Code testing file
from DNAToolkit import *
from utilities import colored
import random

# Creating a random DNA sequence for testing:
randDNAStr = ''.join([random.choice(Nucleotides)
                      for nuc in range(50)])
DNAStr = validateSeq(randDNAStr)

print(f'\nSequence:{colored(DNAStr)}\n')
print(f'[1] + Sequence Length: {len(DNAStr)}\n')
print(colored(f'[2] + Nucleotide Frequency: {countNucFrequency(DNAStr)}\n'))
print(f'[3] + DNA/RNA Transcription: {colored(transcription(DNAStr))}\n')

print(f"[4] + DNA String + Reverse Complement:\n5' {colored(DNAStr)} 3'")
print(f"   {''.join(['|' for c in range(len(DNAStr))])}")
print(f"3' {colored(reverse_complement(DNAStr))} 5'\n")

print(f'[5] + GC Content: {gc_content(DNAStr)}%\n')
print(f'[6] + GC Content in Subsequence k=5: '
      f'{gc_content_sebsec(DNAStr, k = 5)}\n')