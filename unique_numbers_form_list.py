my_list = [1,2,2,4,6,4,6,7,1,9]
new_list = []
for number in my_list:
    if number not in new_list:
        new_list.append(number)

print(new_list)
