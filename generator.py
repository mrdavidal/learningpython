#A simple generator
def gen(my_list):
    for item in my_list:
        yield item

list = ["First", 2, "Third", 4, "Fifth"]

values = gen(list)
# First attempt of retrivieng the items from list
print("First way of accesing the items:", "\n")
print(next(values))
print(next(values))
print(next(values))
print(next(values))
print(next(values))
#second attempt of retrivieng the items from my list
print("Second way of accesing the items:", "\n")
for values in gen(list):
    print(values)
