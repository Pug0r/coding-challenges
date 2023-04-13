data = input()
lower = []
upper = []
odd = []
even = []
for char in data:
    if char.isdigit():
        if char in {'0', '2', '4', '6', '8'}:
            even.append(char)
        else:
            odd.append(char)
    else:
        if char.isupper():
            upper.append(char)
        else:
            lower.append(char)

lower.sort()
upper.sort()
odd.sort()
even.sort()

print(''.join(lower + upper + odd + even))
