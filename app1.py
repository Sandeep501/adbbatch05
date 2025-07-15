# build a calculator app

def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    return a/b

def calculator():
    print("Select Operation: ")
    print("1. Add")
    print("2. Sub")
    print("3. Multiply")
    print("4. Divide")
    
    choice = input("Enter the choice (1|2|3|4): ")
    if choice in ['1', '2', '3', '4']:
        num1 = int(input("Enter First Num: "))
        num2 = int(input("Enter Second Num: "))
        
        if choice == '1':
            print(f"Result: {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {sub(num1, num2)}")
        elif choice == '3':
            print(f"Result: {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {divide(num1, num2)}")
    else:
        print(f"Operation not available for choice {choice}")
            

print(calculator()) 