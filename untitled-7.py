#8
first_max = int(input())
second_max = int(input())

if second_max > first_max:
    first_max, second_max = second_max, first_max

while True:
    num = int(input())
    if num == 0:
        break
    if num > first_max:
        second_max = first_max
        first_max = num
    elif num > second_max:
        second_max = num

print(second_max)