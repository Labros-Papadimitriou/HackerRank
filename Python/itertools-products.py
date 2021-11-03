import itertools

a = list(map(int, input().split(" ")))
b = list(map(int, input().split(" ")))

prd = itertools.product(a, b)
for x in prd:
    print(x, end=" ")
