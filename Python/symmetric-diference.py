m = int(input())
m_roll = set(map(int, input().split()))
n = int(input())
n_roll = set(map(int, input().split()))

total = m_roll.symmetric_difference(n_roll)
l_total = sorted(list(total))
for x in l_total:
    print(x)
