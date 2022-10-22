hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
end_hours = (hour + ((mins + dura) // 60)) % 24
end_mins = (mins + dura) % 60

print(end_hours, ":" , end_mins)
