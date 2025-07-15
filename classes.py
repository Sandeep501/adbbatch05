# python classes

# class Person:
#     def show_details(self):
#         return "This is a person class"

# person1 = Person()
# print(person1.show_details())


class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("I'm the constructor method for the Person class")

    def show_details(self):
        return f"Hello, I'm {self.name} and I'm {self.age} year's old"

person1 = Person("Dileep", 30)
print(person1.show_details())
print("\n")
person2 = Person("Sandeep", 29)
print(person2.show_details())

print(person2.name)

