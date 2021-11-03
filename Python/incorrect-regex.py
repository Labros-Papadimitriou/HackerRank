import re

for _ in range(int(input())):
    try:
        s = re.compile(input())
        is_valid = True
    except re.error:
        is_valid = False
    print(is_valid)
