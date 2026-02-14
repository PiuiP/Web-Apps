n = int(input())
A = list(map(int, input().split()))
first = second = -10**53
for num in A:
    if num > first:
        second = first
        first = num
    elif first > num > second:
        second = num
print(second)