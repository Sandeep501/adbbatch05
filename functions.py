# functions | methods

# name = input("Enter nName: ")

# def funName():
    # code
    
# def add(a, b):
#     return a + b

# print(add(100, 300))
# print(add(10000, 400))



# default parameters

# def greet(age, height, n='Ganesh'):
#     return f"Good Morning {n} and his age is {age} and height is {height}"

# print(greet(n='Kalyan', age=30, height=172))

# print(greet("Kalyan"))

# Arbitrary Arguments

def add_all_nums(*numbers):
    l = numbers
    print(type(l))
    total = sum(numbers)
    return total

# print(add_all_nums(20, 30, 40, 50, 60))
# print(add_all_nums(20, 30, 40, 50, 60, 70, 80))

# Arbitrary KeyWord Arguments

def student_details(**info):
    print(type(info))
    return (info)
    # for key, value in info.items():
    #     print(f"{key}: {value}")
        
# print(student_details(name="Amit", age=30, city="Bangalore"))

# lambda functions -> anonymous functions | single line functions

# def add(a, b):
#     return a+b

add = lambda a, b: a+b
# print(add(10, 20))

even_odd = lambda x: f"{x} is even" if x%2 ==0 else f"{x} is odd"
# print(even_odd(34))
# print(even_odd(11))


# def even_odd(n):
#     if n%2 == 0:
#         print(f"{x} is even")
#     else:
#         print(f"{x} is odd")

dic_items1 = {"one": 1, "two": 2, "three": 3, "four": 4}
dic_items2 = {"five": 5, "six": 6, "seven": 7, "eight": 8}

even_lambda = lambda x: [f"{key}:{value}" for key, value in x.items() if value%2 == 0]

# print(even_lambda(dic_items1))
# print(even_lambda(dic_items2))

# function calling another function

def multiply(a, b):
    return a*b

def area_of_rectangle(length, width):
    return multiply(length, width)

# print(area_of_rectangle(5, 3))


def outer():
    print("This is an outer function")
    
    def inner():
        print("This is an inner function")
    
    print("I'm a part of this function")
    inner()

print(outer())
