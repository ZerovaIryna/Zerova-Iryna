num_array = []
total = 0
print("Будь ласка, введіть 5 натуральних чисел ")
for a in range(5):
    num_array.append(int(input("Введіть число:")))
    if num_array[a] % 2 == 1:
        total += num_array[a]
print("Сума усіх непарних: ",total)
