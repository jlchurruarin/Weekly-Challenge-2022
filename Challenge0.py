# Reto #0
# EL FAMOSO "FIZZ BUZZ"
# Fecha publicación enunciado: 27/12/21
# Fecha publicación resolución: 03/01/22
# Dificultad: FÁCIL
# Enunciado: Escribe un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
# - Múltiplos de 3 por la palabra "fizz".
# - Múltiplos de 5 por la palabra "buzz".
# - Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
#
# Información adicional:
# - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
# - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
# - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
# - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#

for numero in range(1, 101):
    es_multiplo_de_tres = True if numero % 3 == 0 else False
    es_multiplo_de_cinco = True if numero % 5 == 0 else False

    if es_multiplo_de_tres and es_multiplo_de_cinco:
        texto = "fizzbuzz"
    elif es_multiplo_de_tres:
        texto = "fizz"
    elif es_multiplo_de_cinco:
        texto = "buzz"
    else:
        texto = numero

    print(texto)