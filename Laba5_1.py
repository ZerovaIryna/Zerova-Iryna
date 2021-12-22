import random
random_number = random.randint(1,10)
print('Вгадайте число від 1 до 9: ')
guess = 0
while guess!=random_number:
    guess = int(input('Введіть ваше число?: '))
    if guess==random_number:
        print('Вітаю, ви виграли!')
    else:
        print('Ні, спробуйте знову')