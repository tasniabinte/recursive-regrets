t = int(input())
for i in range(t):
    n = int(input())
    name = input()
    if n == 5 and (sorted(name) == sorted("Timur")):
        print("YES")
    else:
        print("NO")
