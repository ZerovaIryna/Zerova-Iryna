print('Програма покаже всі спільні ділені числа на 5 та 7')
for a in range(1500, 2701):
    if a % 5 == 0 and a % 7 == 0:
        print('Число ділиме на 5 та 7:',a)
    elif a % 5 == 0:
        print('Число ділиме на 5:',a)
    elif a % 7 == 0:
        print('Число ділиме на 7:',a)