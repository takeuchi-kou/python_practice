# DNA Toolkit
import collections
from structure import *


# Check the sequence to make sure it is a DNA string
def validateSeq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
        return tmpseq

def countNucFrequency(seq):
    tmpFrqDict = {"A": 0, "C": 0, "G": 0, "T": 0}
    for nuc in seq:
        tmpFrqDict[nuc] += 1
    return tmpFrqDict

def transcription(seq):
    """DNA -> RNA Transcription. Replacing Thymine with Uracil"""
    return seq.replace("T", "U")

def reverse_complement(seq):
    """Swapping adenine with thymine and quanine with cytosine. Reversing newly generated string"""
    return ''.join([DNA_ReverseComplement[nuc] for nuc in seq])