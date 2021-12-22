rech1 = input("Введіть речення:")
slovo = input("Введіть слово, яке ви шукаєте:")
counter = 0
for i in range(len(rech1)):
    if rech1[i] == slovo:
        counter += 1
    elif counter < 1:
        print("Результатів не знайдено :C")
print("Слово, яке ви хочете знайти, трапляється у реченні: ",counter)