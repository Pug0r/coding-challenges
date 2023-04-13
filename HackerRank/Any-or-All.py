# Enter your code here. Read input from STDIN. Print output to STDOUT

num = int(input())
numbers = list(map(int, input().split()))

if all(map(lambda x: True if x > 0 else False, numbers)) and any(map(lambda x: str(x) == str(x)[::-1], numbers)):

    print(True)
else:
    print(False)
