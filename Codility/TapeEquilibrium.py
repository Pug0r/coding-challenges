# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A: list) -> int:
    """ O(n) solution """
    all_sum = sum(A)
    sum_so_far = 0
    min_diff = float('inf') 
    for index, item in enumerate(A[:-1]):
        sum_so_far += item
        min_diff = min(min_diff, abs(2*sum_so_far - all_sum))

    min_diff = min(min_diff, abs(sum_so_far - A[-1]))
    return min_diff
