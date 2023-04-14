# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
  ''' O(nlogn) solution '''
    numbers = list(set(A))
    if 1 not in numbers:
        return 1
    numbers.sort()
    result = 1
    for index, number in enumerate(numbers):
        if number <= 0:
            continue
        else:
            try:
                if numbers[index] + 1 < numbers[index + 1]:
                    return numbers[index] + 1
            except IndexError:
                return numbers[-1] + 1
        
    return result
