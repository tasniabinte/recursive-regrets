k, n, w = map(int, input().split())
total = k * (w * (w + 1) // 2)  
borrow = max(0, total - n)
print(borrow)
