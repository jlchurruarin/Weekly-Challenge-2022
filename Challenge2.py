#
# Reto #2
# LA SUCESIÓN DE FIBONACCI
# Fecha publicación enunciado: 10/01/22
# Fecha publicación resolución: 17/01/22
# Dificultad: DIFÍCIL
#
# Enunciado: Escribe un programa que imprima los 50 primeros números de la sucesión de Fibonacci empezando en 0.
# La serie Fibonacci se compone por una sucesión de números en la que el siguiente siempre es la suma de los dos anteriores.
# 0, 1, 1, 2, 3, 5, 8, 13...
#
# Información adicional:
# - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
# - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
# - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
# - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#

QUANTITY = 50 #Cantidad a imprimir

def next_fib():
    '''
    Función generadora de la seríe de Fibonacci
    '''
    last_numbers = []
    last_numbers.append(1)
    last_numbers.append(1)
    yield 0
    yield 1
    yield 1
    while(True):
        last_numbers.append(sum(last_numbers))
        last_numbers.pop(0)
        yield last_numbers[1]

item_counter = 0
for item in next_fib():
    item_counter += 1
    if item_counter <= QUANTITY:
        print(item_counter, item, sep=": ")
    else:
        break


    

