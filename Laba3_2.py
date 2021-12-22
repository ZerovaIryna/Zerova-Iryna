import math

def p(s):
    print(s)

p('Введіть вхідні параметри a, b та c')

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

D = b**2 - (4 * a * c)

if D > 0:
    x1 = (-b-math.sqrt(D))/2*a
    x2 = (-b+math.sqrt(D))/2*a
    p('x1=', x1,'x2=', x2)
elif D == 0:
    x = (-b)/2*a
    p('x=', x)
elif D < 0:
    p('Немає квадратний коренів в квадратному рівняні :C')
