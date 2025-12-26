import time

print("Welcome to the Calculator!")
def opr():
    print("Operations available: ")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

while True:
    opr()
    oprt = int(input("Choose what to do(sr. no.): "))
    if oprt == 1:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number to be added: "))
        print(f"Result: {a + b}.")
        time.sleep(2)
        while True:
            ans1 = input("Clear?(y/n) ")
            if ans1 == "y":
                opr()
                break
            elif ans1 == "n":
                time.sleep(5)
                continue
        
    elif oprt == 2:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number to be subtracted: "))
        print(f"Result: {a - b}.")
        time.sleep(2)
        while True:
            ans1 = input("Clear?(y/n) ")
            if ans1 == "y":
                opr()
                break
            elif ans1 == "n":
                time.sleep(5)
                continue
        
    elif oprt == 3:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number to be multiplied: "))
        print(f"Result: {a * b}.")
        time.sleep(2)
        while True:
            ans1 = input("Clear?(y/n) ")
            if ans1 == "y":
                opr()
                break
            elif ans1 == "n":
                time.sleep(5)
                continue
        
    elif oprt == 4:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number to be divided: "))
        if b == 0:
            print("Cannot divide by 0.")
            print("Please Retry.")
            time.sleep(2)
            continue
        else:
            print(f"Result: {a / b}.")
            time.sleep(2)
        while True:
            ans1 = input("Clear?(y/n) ")
            if ans1 == "y":
                opr()
                break
            elif ans1 == "n":
                time.sleep(5)
                continue
        
    elif oprt == 5:
        print("Have a great day!")
        exit()
        
    else:
        print("Invalid choice. Please retry.")
