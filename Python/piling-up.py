from collections import deque

t = int(input())
for _ in range(t):
    n = int(input())
    le = deque(map(int, input().split()))
    for i in reversed(sorted(le)):
        if le[0] == i:
            le.popleft()
        elif le[-1] == i:
            le.pop()

    if len(le) == 0:
        print("Yes")
    else:
        print("No")
