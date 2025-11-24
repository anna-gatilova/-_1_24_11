a = int(input())
s = 0
while a != 0:
    if a % 2 == 0:
        s += 1
    a -= 1
print(s)