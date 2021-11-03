x_roll = set(map(int, input().split()))
n = int(input())
sub = {}
tracker = 0
for i in range(n):
    sub[i] = set(map(int, input().split()))
    if not x_roll > sub[i]:
        tracker = 999
        print("False")
        break
if tracker == 0:
    print("True")
