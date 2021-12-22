from os import *
from os.path import isfile, join, isdir

all_elements = list()
files = list()
folders = list()
path = str(input("Вхідний шлях до теки: "))
for element in listdir(path):
    all_elements.append(element)
    if isfile(join(path, element)):
        files.append(element)
    if isdir(join(path, element)):
        folders.append(element)
print("[!] Усі дані")
print(*all_elements, sep = "\n")
print("[!] Тільки папки")
print(*folders, sep = "\n")
print("[!] Тільки файли")
print(*files, sep = "\n")