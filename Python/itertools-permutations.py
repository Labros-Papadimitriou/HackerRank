from itertools import permutations

s, k = input().split()
all = permutations(sorted(s), int(k))
for i in all:
    for x in range(int(k)):
        print(i[x], end="")
    print()
