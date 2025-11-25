#5
a = int(input())
b = 0
while a != 0:
    c = int(input())
    if c == 0:
        break
    if a == c:
        b += 1
        a = int(input())
    else:
        a = c
print(b)