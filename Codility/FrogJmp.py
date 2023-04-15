# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X: int, Y: int, D: int) -> int:
  """ O(1) solution """
    distance = Y - X
    if distance % D == 0:
        return distance // D
    else:
        return (distance // D) + 1
