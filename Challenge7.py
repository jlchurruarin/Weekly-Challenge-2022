#
# Reto #7
# CONTANDO PALABRAS
# Fecha publicación enunciado: 14/02/22
# Fecha publicación resolución: 21/02/22
# Dificultad: MEDIA
#
# Enunciado: Crea un programa que cuente cuantas veces se repite cada palabra y que muestre el recuento final de todas ellas.
# - Los signos de puntuación no forman parte de la palabra.
# - Una palabra es la misma aunque aparezca en mayúsculas y minúsculas.
# - No se pueden utilizar funciones propias del lenguaje que lo resuelvan automáticamente.
#
# Información adicional:
# - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
# - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
# - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
# - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#
#

import re

def count_words(text: str)-> dict:
    '''
    Función que devuelve un diccionario que cuenta cada palabras de un string y las veces que se repite

    Recibe por parametro el string a verificar

    Devuelve un diccionario, donde las claves son las diferentes palabras y su valor la cantidad de veces que aparece
    '''

    #Solo se tienen en cuenta las letras de la A a la Z y las letras con tilde
    lista_de_palabras = re.findall(r"([a-zA-Záéíóú]+)", text) 
    dict_palabras = {}
    for palabra in lista_de_palabras:
        palabra = palabra.lower()
        if palabra in dict_palabras:
            dict_palabras[palabra] += 1
        else:
            dict_palabras[palabra] = 1
    
    return dict_palabras

def print_dict(dict: dict):
    '''
    Funcion que imprime un diccionario

    Realiza una impresion de la clave y su valor por linea
    '''
    for item in dict:
        print("{0}: {1}".format(item, dict[item]))


print_dict(count_words("Texto de prueba, una sola palabra aparece dos veces en este texto, los numeros, por ejemplo: 20, son ignorados"))
