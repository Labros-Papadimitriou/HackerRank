a = int(input())
a_roll = set(map(int, input().split()))
b = int(input())
b_roll = set(map(int, input().split()))

print(len(a_roll.difference(b_roll)))
