import math
import os
import random
import re
import sys
from collections import defaultdict

if __name__ == '__main__':
    d = defaultdict(int)
    s = sorted(input())
    for letter in s:
        d[letter] += 1

    di = dict(d)
    li = []
    keys = []
    values = []

    while len(li) < 3:
        max_key = max(di, key=di.get)
        max_value = max(di.values())
        di.pop(max_key)
        li.append("COUNTER TO STOP LOOPING")
        print(max_key, max_value)
