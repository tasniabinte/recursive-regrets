num = int(input())
countLucky = 0
for i in str(num):
  if i in '47':
    countLucky += 1

if countLucky == 4 or countLucky == 7: print('YES')

else: print('NO')  
