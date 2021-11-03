for _ in range(int(input())):
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero")
    except ValueError as detail:
        print(f"Error Code: {detail}")
