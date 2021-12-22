first_num = int(input('Введіть перше число: '))
second_num = int(input('Введіть друге число: '))
if first_num % second_num or second_num % first_num == 0:
    print('Ці числа кратні')
else:
    print('Ці числа не кратні')