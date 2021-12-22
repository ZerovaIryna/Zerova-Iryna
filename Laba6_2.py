print('Програма виконає всі можливі перестановки')
import itertools
l = input('Введіть значення: ')
p = itertools.permutations(l)
for a in list(p):
    print(a)