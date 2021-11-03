import sys

n = int(input())
li = list(map(int, input().split()))
if all([i > 0 for i in li]):
    for i in li:
        if str(i) == str(i)[::-1]:
            print("True")
            sys.exit()
print("False")
