t = int(input())
for i in range(t):
    n = int(input())
    n_roll = set(map(int, input().split()))
    b = int(input())
    b_roll = set(map(int, input().split()))
    if n_roll.issubset(b_roll):
        print("True")
    elif not n_roll.issubset(b_roll):
        print("False")
