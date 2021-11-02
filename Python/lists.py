if __name__ == '__main__':
    n = int(input())
numbers = []
for _ in range(n):
    first_num = 0
    sec_num = 0
    option = input()
    sum_items = [int(i) for i in option.split() if i.isdigit()]
    if "insert" in option:
        first_num = sum_items[0]
        sec_num = sum_items[1]
        numbers.insert(first_num, sec_num)
    elif "print" in option:
        numbers = [int(items) for items in numbers]
        print(numbers)
    elif "remove" in option:
        first_num = sum_items[0]
        numbers.remove(first_num)
    elif "append" in option:
        first_num = sum_items[0]
        numbers.append(first_num)
    elif "sort" in option:
        numbers.sort()
    elif "pop" in option:
        numbers.pop()
    elif "reverse" in option:
        numbers.reverse()
