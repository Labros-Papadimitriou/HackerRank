def average(array: int) -> float:
    total = set()
    for i in array:
        total.add(i)
    summary = sum(total)
    length = len(total)
    av = summary / length
    return float("{:.3f}".format(av))
