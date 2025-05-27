year = int(input())
distYear = year + 1
if 1000 <= year <= 9000:
  while True:
    if len(set(str(distYear))) < 4:
      distYear += 1
      
 
    else:
      print(distYear)
      break
