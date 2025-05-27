word = input()
low_cnt = 0
up_cnt = 0
for i in word:
  if i.islower():
    low_cnt += 1

  else:
    up_cnt += 1

if low_cnt == up_cnt:
  word = word.lower()

elif low_cnt > up_cnt:
  word = word.lower()

else:
  word = word.upper()

print(word)    
