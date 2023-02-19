

#
# Reto #12
# ¿ES UN PALÍNDROMO?
# Fecha publicación enunciado: 21/03/22
# Fecha publicación resolución: 28/03/22
# Dificultad: MEDIA
#
# Enunciado: Escribe una función que reciba un texto y retorne verdadero o falso (Boolean) según sean o no palíndromos.
# Un Palíndromo es una palabra o expresión que es igual si se lee de izquierda a derecha que de derecha a izquierda.
# NO se tienen en cuenta los espacios, signos de puntuación y tildes.
# Ejemplo: Ana lleva al oso la avellana.
#
# Información adicional:
# - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
# - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
# - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
# - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#
#/

import unicodedata
import re

def is_palindrome(text: str) -> bool :
    '''
    Función que verifica si un texto es palindromo

    Devuelve verdadero si lo es falso si no
    '''

    #Normalizamos texto y borramos espacios
    text_normalized_without_spaces = normalize_string(text).replace(" ", "")
    #Borramos todos los caracteres que no sean letras
    text_alphabetic_without_spaces = re.sub("[^a-z]", "", text_normalized_without_spaces)

    return text_alphabetic_without_spaces == text_alphabetic_without_spaces[::-1]


def normalize_string(text: str) -> str:
    '''
    Función que normaliza un texto
    '''

    # Dividimos el texto por los caracteres "ñ" para evitar perder el caracter
    split_text = re.split(r"ñ", text.lower())

    return_text = []
    for text_part in split_text:
        return_text.append(unicodedata.normalize("NFKD", text_part)\
            .encode("ascii","ignore").decode("ascii"))

    # Retornamos el texto uniendolo por el caracter "ñ"
    return "ñ".join(return_text)