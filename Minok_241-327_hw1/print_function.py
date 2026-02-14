n = int(input())
if (n < 1  or n > 20):
    print("1 <= N <= 20")
else:
    for i in range(1, n+1):
        print(i, end='')