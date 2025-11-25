#9
max_num = 0
count_max = 0

while True:
    num = int(input())
    if num == 0:
        break
    if num > max_num:
        max_num = num
        count_max = 1
    elif num == max_num:
        count_max += 1

print(count_max)