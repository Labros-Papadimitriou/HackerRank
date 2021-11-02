def merge_the_tools(word: str, number: int) -> None:
    """Example: word--> AABCAAADA   number--> 3
    print --> AB CA AD (but on a new line each)

    :param word: The string to analyze.
    :param number: The size of substrings to analyze.
    """
    for i in range(0, len(word), number):
        sub = word[i:i + number]
        substring = ""
        for j in range(0, len(sub)):
            if substring.count(sub[j]) < 1:
                substring += sub[j]
        print(substring)
