# Imports
from itertools import permutations
import random

# Declaramos las variables
number = random.randint(0,99)
intentos = 0
givenNumber = input('Adivina el número: ')

# Main Code
while not givenNumber.isdigit():
    givenNumber = input('Introduzca un número válido: ')
while int(givenNumber) != number:
    if int(givenNumber) > number:
        intentos = intentos + 1
        print('No has acertado, te has pasado.\nYa llevas ' + str(intentos) + ' intentos.')
        givenNumber = input('Intentalo de nuevo: ')
    elif int(givenNumber) < number:
        intentos = intentos + 1
        print('No has acertado, te has quedado corto.\nYa llevas ' + str(intentos) + ' intentos.')
        givenNumber = input('Intentalo de nuevo: ')
if int(givenNumber) == number:
    print('¡Has acertado! Lo ha conseguido en ' + str(intentos) + ' intentos.')

# End