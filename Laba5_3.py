print('Програма надрукує числа від 0 до 7, крім 3 та 6')
for a in range(0,8):
    if a == 3:
        continue
    if a == 6:
        continue
    print('Числа від 0 до 7, окрім 3 та 6:',a)
print('Кінець')