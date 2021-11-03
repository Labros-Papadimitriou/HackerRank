n = int(input())
n_roll = set(map(int, input().split()))
b = int(input())
b_roll = set(map(int, input().split()))

total = n_roll.intersection(b_roll)
print(len(total))
