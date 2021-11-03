n, m = list(map(int, input().split()))
array = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))

happiness = 0
sadness = 0

for i in array:
    if i in a:
        happiness += 1
    elif i in b:
        sadness += 1

print(happiness - sadness)
