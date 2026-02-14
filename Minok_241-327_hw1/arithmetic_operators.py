a, b = int(input()), int(input())
if ((a < 1 or a > 10**10) or ((b< 1 or b > 10**10))):
    print ("1 <= A <= 10^10 AND 1 <= B <= 10^10")
else:
    print (a + b)
    print (a - b)
    print (a * b)