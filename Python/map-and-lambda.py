cube = lambda x: x**3
def fibonacci(n):
    li = [0]
    lo = []
    x = 1
    if n == 0:
        return lo
    else:    
        while len(li) < n:
            li.append(x)
            x += li[-2]
        return li
 
