s = sorted(input())
upperalpha = []
loweralpha = []
odd = []
even = []
for char in s:
    if char.isalpha() and char.isupper():
        upperalpha.append(char)
    elif char.isalpha() and char.islower():
        loweralpha.append(char)
    elif char.isdigit() and int(char) % 2 == 0:
        even.append(char)
    elif char.isdigit() and int(char) % 2 != 0:
        odd.append(char)
print("".join(loweralpha + upperalpha + odd + even))
