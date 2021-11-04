import re

for _ in range(int(input())):
    s = input()
    print(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', s))
