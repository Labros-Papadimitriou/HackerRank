def print_formatted(number):
    width = len(bin(n).lstrip('0b'))
    for i in range(1, number + 1):
        print(f"{i:{width}} {oct(i).lstrip('0o'):>{width}} {(hex(i).lstrip('0x')).upper():>{width}} {bin(i).lstrip('0b'):>{width}}")
