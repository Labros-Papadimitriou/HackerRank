def mutate_string(string, position, character):
    listed_s = list(string)
    listed_s[position] = character
    result = "".join(listed_s)
    return result
