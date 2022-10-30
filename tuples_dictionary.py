#we define an empty dictionary
school_class = {}

while True:
    name = input("Enter the student's name: ")#input name(key)
    if name == '': #condition for the while to stop
        break

    score = int(input("Enter the student's score (0-10): "))#input score(value)
    if score not in range(0, 11): #condition for the while to stop
	    break

    if name in school_class: #check if the key is in dictionary
        school_class[name] += (score,) #key equals with tuples values
    else:
        school_class[name] = (score,)#new key equals with tuples values

for name in sorted(school_class.keys()): #iterating through the dictionary
    adding = 0
    counter = 0
    for score in school_class[name]: #iterating through tuples
        adding += score #sum of all values
        counter += 1 #sum of number of values
    print(name, ":", adding / counter) # printing key and average score(value)
