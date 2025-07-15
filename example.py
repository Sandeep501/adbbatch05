name = input("Enter Name: ")
age = input("Enter Age: ")
# print(type(name))
print("Good Morning", name, "your age is:", age)

print("Good Morning {PersonName}, your age is: {PersonAge}".format(PersonName=name, PersonAge=age))

print(f"Good Morning {name}, your age is: {age}")

# modern approach -> string formaters

# types
# .format()
# f""

# print("Good Morning {0}, ".format(name))