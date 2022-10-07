try:
        while True:
            a = input("Enter 'a' value: ")
            b = input("Enter 'b' value: ")
            print(int(a)/int(b))
except ZeroDivisionError:
    print("Division by zero not allowed")
