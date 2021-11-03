a = int(input())
a_roll = set(map(int, input().split()))
b = int(input())
b_roll = set(map(int, input().split()))

print(len(a_roll.symmetric_difference(b_roll)))
