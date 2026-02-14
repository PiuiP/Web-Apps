n, m = map(int, input().split())

items = []
for _ in range(m):
    name, w, v = input().split()
    w = int(w)
    v = int(v)
    
    if w == 0:
        ratio = float('inf')
    else:
        ratio = v / w
    
    items.append((ratio, name, w, v))


items.sort(reverse=True)

capacity = n
loaded = []

for ratio, name, w, v in items:
    if capacity <= 0:
        break
    
    if w <= capacity:
        loaded.append((name, w, v))
        capacity -= w
    else:
        fraction = capacity / w
        loaded.append((name, capacity, v * fraction))
        capacity = 0


loaded.sort(key=lambda x: x[2], reverse=True)
for name, weight, value in loaded:
    print(f"{name} {weight:.2f} {value:.2f}")