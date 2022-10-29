def is_triangle(a,b,c):
    return a + b > c and a + c > b and b + c > a

a = float(input("Enter a value for the first side:"))
b = float(input("Enter a value for the second side: "))
c = float(input("Enter a value for the third side:"))

print(is_triangle(a,b,c))
