a = int(input())
a_roll = set(map(int, input().split()))
b = int(input())
b_roll = set(map(int, input().split()))

total = len(a_roll.union(b_roll))
print(total)
