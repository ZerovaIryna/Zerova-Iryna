rech1 = str(input('Введіть речення:\n'))
slova = 1
print('Букв у реченні:',len(rech1))
for a in range(len(rech1)):
    if rech1[a] == " ":
        slova += 1
print("Слів у реченні:",slova)