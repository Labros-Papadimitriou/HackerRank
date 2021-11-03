from itertools import combinations_with_replacement

s, k = map(str, input().split(" "))
combs = combinations_with_replacement(sorted(s), int(k))
for i in combs:
    print(*i, sep='')
