rech1 = str(input("Введіть перше речення: "))
rech2 = str(input("Введіть друге речення: "))
if  rech1 == rech2:
     print("Речення ідентичні")
elif len(rech1) == len(rech2):
     print("Довжина речень одинакова, але контент різний")
elif len(rech1) > len(rech2):
     print("Речення 1 більше за речення 2")
elif len(rech1) < len(rech2):
     print("Речення 2 більше за речення 1")
