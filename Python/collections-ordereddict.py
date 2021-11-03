from collections import OrderedDict

n = int(input())
di = {}
for i in range(n):
    *item, price = input().split(" ")
    final = ""
    for i in item:
        final += i + " "
    if final in di.keys():
        di[final] += int(price)
        continue
    di[final] = int(price)

for key, val in di.items():
    print(f"{key}{val}")
