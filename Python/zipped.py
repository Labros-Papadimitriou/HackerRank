n, x = map(int, input().split())
li = []
for _ in range(x):
    li.append(map(float, input().split()))
    
for i in zip(*li):
    print(sum(i) / x)
