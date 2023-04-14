# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import defaultdict

def solution(N: int, A: list) -> list:
    ''' O(n) solution '''
    counter = defaultdict(int)
    max_value = 0 
    last_maxed = 0
    for item in A:
        if item == N + 1:
            last_maxed = max_value
            # Reset the additions to every counter
            counter = defaultdict(int)
        else:
            counter[item-1] += 1
            max_value = max(max_value, last_maxed + counter[item-1])
    result = [last_maxed for _ in range(N)]
    # Add values that remain in counter after last max counter operation
    for index, value in counter.items():
        result[index] += value
    return result
