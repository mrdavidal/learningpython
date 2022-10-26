def unique_numbers(list):
    list_r = []
    for number in list:
        if number not in list_r:
            list_r.append(number)
    return list_r

print(unique_numbers([1,1,2,88,8,9,5,2,4,88,9,0]))
