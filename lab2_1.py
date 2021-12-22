first_num = float(input("Введіть перше число:"))
second_num = float(input("Введіть друге число:"))
total = first_num*second_num
if first_num == second_num:
    print("Це квадрат і площа="+str(total))
else:
    print("Площа =" + str(total))