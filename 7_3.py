import pickle
import os

path = os.getcwd()

dictionary = dict()

file = open('файл.txt','r')
key = file.name
dictionary[key] = file.read()

first_file = open('перший.txt','r')
key = first_file.name
dictionary[key] = first_file.read()

second_file = open('другий.txt','r')
key = second_file.name
dictionary[key] = second_file.read()

with open('словничок' + '.pkl', 'wb+') as k:
    pickle.dump(dictionary, k)