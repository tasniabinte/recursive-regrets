n, m , a = map(int, input().split())
numOfTiles = ((n + a -1) // a) * ((m + a - 1) // a)
print(numOfTiles)
