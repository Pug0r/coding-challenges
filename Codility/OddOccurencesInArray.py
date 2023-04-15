# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import Counter

def solution(A):
    """ O(n) solution """
    counter = Counter(A)
    for key, value in counter.items():
        if value % 2 != 0:
            return key
