import string
import sys


def isPangram(string, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)
    return alphaset <= set(string.lower())
