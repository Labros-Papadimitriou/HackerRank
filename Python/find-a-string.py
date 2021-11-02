def count_substring(string, sub_string):
    total = 0
    for i in range(0, len(string) + 1):
        count = string[i:i + len(sub_string)].count(sub_string)
        total += count
    return total
