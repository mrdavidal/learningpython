my_list = [1,1,2,4,4,2,6,4,1,9,7,9]
counter = 0
i = 1
while counter < len(my_list):
    while i < len(my_list):
        if my_list[counter] == my_list[i]:
            del my_list[i]
        i += 1
    i = counter + 2
    counter += 1
print(my_list)
