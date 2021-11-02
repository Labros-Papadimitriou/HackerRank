def door_mat(height, width):
    pat = ".|."
    cen = "WELCOME".center(width, "-")
    for i in range(1, height - 1, 2):
        upp = (pat * i).center(width, "-")
        print(upp)
    print(cen)
    for j in range(height - 2, 0, -2):
        down = (pat * j).center(width, "-")
        print(down)


n, m = map(int, input().split())
while (n % 2 == 0) or n <= 5 or n >= 101 or m != n * 3:
    print("Please first enter an odd between 5 and 101"
          " and then 3 times same number")
    n, m = map(int, input().split())

door_mat(n, m)
