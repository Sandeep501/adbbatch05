# 1. list -> just like array [1, 2, 3, 4, 'a', 2.22, True, [1, 4, 5], ('d', 'f')]
# 2. tuple -> (1, 2, 3, 4, 'a', 2.22, True, [], ())
# 3. set -> {1, 1, 2, 3, 4, [], (), {}} -> this does not allow duplicate values -> {1, 2, 3, 4, [], (), {}}
# 4. dictionary -> {
#     "key": "value",
#     "name": "sandeep",
#     "subjects": ["Maths", "Physics", "Scine"],
#     "Languages": {"Telugu", "Kannada", "Hindi"},
# }

# mutable vs immutable

names = ["Rohith", "Arjun", "Ashok"] # -> define list

cities = list(("Bangalore", "Delhi", "Hyderabad"))

ages = list({12, 14, 15})

# add items into list
names.append("Farooq")
print(names)

# modifying list values
names[0] = "Kalyan"
print(names)

# remove item
names.remove("Arjun")
print(names)

print(names.index("Ashok"))


# print(type(names), type(cities), type(ages))


define tuple
cities = ("Bangalore", "Hyderabad", "Jaipur")
print(type(cities))
print(cities)
print(cities[1])

define sets

cities = {"Bangalore", "Hyderabad", "Jaipur"}
print(type(cities))
print(cities)


cities = {"Bangalore", "Hyderabad", "Jaipur", "Hyderabad", "Hyderabad"}
print(cities)

cities.add("Delhi")
print(cities)

cities.remove("Hyderabad")
print(cities)

# print(cities[0])

values = {
    1, 20.334, 34.33377477423262, True, 
    "Dog", 
    'f', 
    'f', 
    True, 
    (1, 2, 3, 4), 
    frozenset({1, 1, 1}),
}
print(values)


# dict

students = {
    "name": "Kalyan",
    "rollNo": 100,
    "Subjects": ["Telugu", "English", "Maths", "Science"],
    "Grade": 7
}

print(students["Grade"])
print(students["Subjects"][2])

print(students.get("Grade"))
print(students.get("Marks", "Not Found"))

students["name"] = "Rohith"
print(students)

# del students["Grade"]
# print(students)

# subjects = students.pop("Subjects")
# print(students)

# print(subjects)

print(students.keys())

print(students.values())

print(students.items())


