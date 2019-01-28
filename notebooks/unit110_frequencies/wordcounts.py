#!/usr/bin/env python3

from collections import Counter
import re


def tokenize(the_string):
    """Convert string to list of words"""
    return re.findall(r"\w+", the_string)


def tokenize_file(the_file):
    """Read file as string and tokenize it"""
    with open(the_file, mode="r", encoding="utf-8") as text:
        return tokenize(text.read())


# define a variable for each token list
hamlet = Counter(tokenize_file("hamlet_clean.txt"))
faustus = Counter(tokenize_file("faustus_clean.txt"))
mars = Counter(tokenize_file("mars_clean.txt"))
