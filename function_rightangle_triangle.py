def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b

def is_rightangle_triangle(a,b,c):
    if not is_a_triangle(a,b,c):
        return False
    if c > a and c > b:
        return a ** 2 + b ** 2 == c ** 2
    if b > a and b > c:
        return a ** 2 + c ** 2 == b ** 2
    if a > b and a > c:
        return b ** 2 + c ** 2 == a ** 2
    return False
print(is_rightangle_triangle(5, 3, 4))
print(is_rightangle_triangle(1, 1, 1))
