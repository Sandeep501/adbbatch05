# nested functions

def greet(name):
    def message():
        print(f"Hello, Good Morning {name}")
    message()
    
# print(greet("Harish"))

# print(message())


def make_multiplier(x):
    def multiply(y):
        return x*y
    return multiply

# times3 = make_multiplier(3)
# print(times3(y=10))

# times5 = make_multiplier(5)
# print(times5(8))





