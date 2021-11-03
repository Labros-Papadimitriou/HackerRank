from itertools import product

k, m = map(int, input().split(" "))
s = []
for i in range(k):
    li = list(map(int, input().split(" ")))[1:]
    s.append(map(lambda x: x**2, li))
print(max(map(lambda x: sum(x)%m, product(*s))))
