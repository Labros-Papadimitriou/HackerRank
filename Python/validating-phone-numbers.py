import re

for _ in range(int(input())):
    number = input()
    if re.match(r'[789]\d{9}$', number):
        print("YES")
    else:
        print("NO")
