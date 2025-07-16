# try except - error handling

# Basic Try-Except

try:
    num = int(input("Enter a Num: "))
    result = 10/num
    print(result)
except ValueError:
    print("Input is invalid, enter only integers > 1")
except ZeroDivisionError:
    print("You can't divide by zero!")
finally:
    print("This always runs")

# custom error handling
class NegativeNumError(Exception):
    pass
    
    
try:
    num = int(input("Enter a Num: "))
    if num < 0:
        raise NegativeNumError("Negative Numbers are not allowed!!")
    result = 10/num
    print(result)
except Exception as e:
    print(f"Exception : {e}")
