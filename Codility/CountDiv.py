# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# Formulas derived from simple arithmetic series properties
def solution(A: int, B: int, K: int) -> int:
  """ O(1) solution """
    if A % K == 0 and  B % K == 0:
        return ((B - A) // K) + 1
    # If either side is not divisible, one has to make sure one starts (and ends) on a number divisible by K
    elif A % K == 0:
        return (((B - (B % K)) - A ) + K) // K
    elif B % K == 0:
        return (B  - (A + (K - (A % K))) + K) // K
    else:
        return ((B - (B % K)) - (A + (K - (A % K))) + K) // K
