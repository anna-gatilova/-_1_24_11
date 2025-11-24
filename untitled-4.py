a = int(input())
count = 0
while True:
    s = int(input())
    if s == 0:
        break
    if s > a:
        count += 1
    a = s
print(count)