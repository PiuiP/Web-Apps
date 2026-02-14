a, b = int(input()), int(input())
try:
    print(a//b)
    print(a/b)
except ZeroDivisionError:
    print("undefined: division by zero is not allowed")
    print("undefined: division by zero is not allowed")