def ZeroDivisonError(value1, value2):
    try:
        print(int(a)/int(b))
    except ZeroDivisionError:
        print("Division by zero not allowed")

if __name__ == "__main__":
    while True:
        a = input("Enter 'a' value: ")
        b = input("Enter 'b' value: ")
        ZeroDivisonError(a, b)