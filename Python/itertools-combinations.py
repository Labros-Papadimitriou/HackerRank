from itertools import combinations

s, k = map(str, input().split(" "))
for i in range(1, int(k) + 1):
    combs = list(combinations(sorted(s), i))
    for j in combs:
        print(*j, sep="")
