import re

for _ in range(int(input())):
    s = input()
    pattern_1 = re.compile("abcdefghijklmnopqrstuvwxyz")
    pattern_2 = re.compile(".-+")
    if pattern_1.search(s) is not None:
        print("False")
        continue
    elif pattern_2.match(s) is not None:
        print("False")
        continue
    elif s.count(".") > 1:
        print("False")
        continue
    elif s.count(".") == 0:
        print("False")
        continue
    elif len(s.split(".")[1]) < 1:
        print("False")
        continue
    else:
        try:
            float(s)
            print("True")
        except:
            print("False")
