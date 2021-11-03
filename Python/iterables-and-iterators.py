from itertools import combinations

n = int(input())
letters = list(map(str, input().split(" ")))
k = int(input())

combs = list(combinations(letters, k))

count = 0
for x in combs:
    if "a" in x:
        count += 1

print(round(count / len(combs),3))
