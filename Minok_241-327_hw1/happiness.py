n, m = map(int, input().split())
arr = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))
    
happiness = sum(1 for num in arr if num in A) - sum(1 for num in arr if num in B)
print(happiness)