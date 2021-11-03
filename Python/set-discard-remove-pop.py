n = int(input())
s = set(map(int, input().split()))
com = int(input())

for _ in range(com):
    option = input()
    for i in option:
        if i.isdigit():
            number = int(i)
    if "pop" in option:
        s.pop()
    elif "remove" in option:
        s.remove(number)
    elif "discard" in option:
        s.discard(number)
print(sum(s))
