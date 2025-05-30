n = int(input())
count = 0
for i in range(n):
  lst = list(map(int, input().split()))
  if sum(lst) >= 2:
    count += 1

print(count)    
