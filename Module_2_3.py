my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
x = len(my_list)
y = 0

while y < x:
    a = my_list[y]
    if a == 0:
        y = y + 1
    elif a > 0:
        print(a)
        y = y+1
    else:
        break