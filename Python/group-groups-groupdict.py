import re

s = input()
s = re.search(r'([a-z0-9])\1+', s)
try:
    print(s.group(1))
except AttributeError:
    print(-1)
