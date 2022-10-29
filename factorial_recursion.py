def factorial(n):
    if n < 0:
        return
    if n < 2:
        return 1
    return n * factorial(n - 1)

for n in range(1, 6): # testing
    print(n, factorial(n))
