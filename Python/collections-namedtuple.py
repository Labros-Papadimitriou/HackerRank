from collections import namedtuple

n = int(input())
columns = input()

Student = namedtuple('Student', columns)
total = 0
for _ in range(n):
    std = Student(*input().split())
    total += int(std.MARKS)
print(f"{total/n:.2f}")
