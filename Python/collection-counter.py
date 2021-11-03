from collections import Counter

shoes = int(input())
avail_size = Counter(map(int, input().split(" ")))
customers = int(input())
earn = 0
for _ in range(customers):
    size, price = map(int, input().split(" "))
    if avail_size[size]:
        earn += price
        avail_size[size] -= 1    
print(earn)
