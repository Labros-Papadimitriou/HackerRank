from collections import deque

n = int(input())
d = deque()
for _ in range(n):
    oper = list(map(str, input().split()))
    if len(oper) == 2:
        if oper[0] == "append":
            d.append(int(oper[1]))
        elif oper[0] == "appendleft":
            d.appendleft(int(oper[1]))
    elif len(oper) == 1:
        if oper[0] == "pop":
            d.pop()
        elif oper[0] == "popleft":
            d.popleft()
for i in d:
    print(i, end=" ")
