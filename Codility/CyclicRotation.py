# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    if len(A) == 0 or K == 0 or K == len(A):
        return A
    cur_list = A.copy()
    for _ in range(K):
        tmp = [cur_list[-1]]
        for item in cur_list[:-1]:
            tmp.append(item)
        cur_list = tmp

    return cur_list
