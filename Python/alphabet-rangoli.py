def print_rangoli(size):
    alp = "abcdefghijklmnopqrstuvwxyz"
    width = (size * 4) - 3
    for j in range(size - 1, 0, -1):
        upp = "-".join(alp[size - 1:j:-1] + alp[j:size])
        print(upp.center(width, "-"))
    for i in range(size):
        down = "-".join(alp[size - 1:i:-1] + alp[i:size])
        print(down.center(width, "-"))
