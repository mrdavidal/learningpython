def factorial_function(n):
    if n < 0:
        return
    if n < 2:
        return 1
    n_factorial = 1
    for i in range(2,n + 1):
        n_factorial *= i
    return n_factorial

for n in range(1, 10): # testing
    print(n, factorial_function(n))
