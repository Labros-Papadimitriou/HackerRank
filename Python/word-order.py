from collections import defaultdict

d = defaultdict(int)
n = int(input())
for i in range(n):
    d[input()] += 1

print(len(d))
for j in d:
    print(d[j], end=" ")
