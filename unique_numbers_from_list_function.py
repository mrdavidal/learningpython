def unique_numbers(list):
    i = 0
    counter = 1
    while i < len(list):
        while counter < len(list):
            if list[i] == list[counter]:
                del list[counter]
            counter += 1
        i += 1
        counter = i + 2
    return list

print(unique_numbers([1,1,2,88,8,9,5,2,4,88,9,0]))
