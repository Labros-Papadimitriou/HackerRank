import re
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
print(*re.findall("(?=[%s]([%s]{2,})[%s])" % (c, v, c), input(), re.I) or [-1], sep="\n")
