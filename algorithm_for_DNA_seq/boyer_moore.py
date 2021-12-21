# preprocessing of pattern and string
# https://www.cambridge.org/core/books/algorithms-on-strings-trees-and-sequences
import string

def z_array(s):
    """Use Z algorithm to preprocess s"""
    assert len(s) > 1
    z = [len(s)] + [0] * (len(s)-1)