number = []
n = int(input("Enter the number of elements:"))
for j in range(n):
    to_add = int(input("Type the numbers. Of them the even ones will be displayed:"))
    number.append(to_add)
even = [i % 2 == 0 for i in number]
i = 0
for x in range(len(even)):
    if even[x] == True:
        even[x] = number[x]
while i < len(even):
    if even[i] == False:
        del even[i]
    i+=1
print(even)
