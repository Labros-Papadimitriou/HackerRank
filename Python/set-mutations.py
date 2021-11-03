elements_a_roll = int(input())
a_roll = set(map(int, input().split()))
other_rolls = int(input())

for i in range(other_rolls):
    comm, val = input().split()
    other_set = set(map(int, input().split()))
    if comm == 'intersection_update':
        a_roll.intersection_update(other_set)
    elif comm == 'update':
        a_roll.update(other_set)
    elif comm == 'difference_update':
        a_roll.difference_update(other_set)
    elif comm == 'symmetric_difference_update':
        a_roll.symmetric_difference_update(other_set)

print(sum(a_roll))
