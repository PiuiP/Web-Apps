n = int(input())
if (n < 1  or n > 20):
    print("1 <= N <= 20")
else:
    i = 0
    while (i < n):
        print(i**2)
        i += 1