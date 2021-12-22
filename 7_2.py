import os

path = os.getcwd()
file = open('файл.txt', 'w+')
text = ['триста вісімдесят пять', 'АЕЕ']

for line in text:
    file.write(line + '\n')

file = open('файл.txt','r')
first = open('перший.txt','w+')
second = open('другий.txt','w+')

data = file.read()

first_line = data.split('\n', 1)[0]
second_line = data.split('\n', 2)[1]

first.write(first_line)
second.write(second_line)

print("Розмір файла: %d байт" %os.path.getsize(path))