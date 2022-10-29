def fibonaci(n):
    if n < 1:
        return
    if n < 3:
        return 1
    first_fib = 1
    second_fib = 1
    sum = 0
    for i in range(3, n + 1):
        sum = first_fib + second_fib
        first_fib = second_fib
        second_fib = sum
    return sum

for n in range(1, 10): # testing
    print(n, "->", fibonaci(n))
