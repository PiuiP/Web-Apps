n = int(input())
if (n < 1 or n > 100):
    print("1 <= N <= 100")
elif (n % 2 != 0) or (n % 2 == 0 and 6 <= n <= 20):
    print("Weird")
elif (n % 2 == 0) and (n > 20 or 2 <= n <= 5):
    print("Not Weird") 