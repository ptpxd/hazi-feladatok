def ZeroDivisonError(value1, value2):
    try:
        print(int(a)/int(b))
    except ZeroDivisionError:
        print("Division by zero not allowed")
while True:
    a = input("Enter 'a' value: ")
    b = input("Enter 'b' value: ")
    ZeroDivisonError(a, b)

