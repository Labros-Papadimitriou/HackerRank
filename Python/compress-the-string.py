from itertools import groupby

s = input()
for key, group in groupby(s):
    a = list(group)
    print(f"({len(a)}, {key})", end=" ")
