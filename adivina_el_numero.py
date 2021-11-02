import random

number = random.randint(0,99)

givenNumber = input('Adivina el número: ')
while not givenNumber.isdigit():
    givenNumber = input('Introduzca un número válido: ')
