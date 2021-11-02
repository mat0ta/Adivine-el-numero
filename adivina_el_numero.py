# Imports
from itertools import permutations
import random
# Declaramos las variables
number = random.randint(0,99)
intentos = 0

# Main Code
givenNumber = input('Adivina el número: ')
while not givenNumber.isdigit():
    givenNumber = input('Introduzca un número válido: ')
if int(givenNumber) != number:
    if int(givenNumber) > number:
        intentos =+ 1
        print('No has acertado, te has pasado.\nYa llevas ' + str(intentos) + ' intentos.')
    elif int(givenNumber) < number:
        intentos =+ 1
        print('No has acertado, te has quedado corto.\nYa llevas ' + str(intentos) + ' intentos.')
if int(givenNumber) == number:
    print('Has acertado! Lo ha conseguido en ' + str(intentos) + ' intentos.')