my_line = str(input("Введіть речення:"))
slovo = str(input("Введіть слово, яке ви хочете знайти у реченні:"))
if slovo in my_line or my_line in slovo:
    print("Слово, яке ви хочете знайти, є у реченні")
else:
    print("Результатів немає")