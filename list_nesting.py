rows = int(input("Enter the number of rows to be created:"))
collums = int(input("Enter the number of collums to be created:"))
element = "."
structure = [[element for i in range(collums)]for j in range(rows)]

for x in range(len(structure)):
    for k in range(len(structure[x])):
        print(structure[x][k], end= " ")
    print()
