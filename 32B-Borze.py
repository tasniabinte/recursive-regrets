m = input()
output = ''
j = 1
i = 0
while j <= len(m):
  if m[i] == '.':
    output += '0'
    j += 1
    i += 1

  elif m[i] == '-' and m[j] == '.':
    output += '1'
    i += 2
    j += 2

  else:
    output += '2'
    i += 2
    j += 2


print(output)
