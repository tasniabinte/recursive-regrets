k, r = map(int, input().split())
temp = k
cnt = 1
while True:
  if ((k - r) % 10) == 0 or k % 10 == 0:
    print(cnt)
    break

  else:
    k += temp
    cnt += 1
