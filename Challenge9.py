
#
# Reto #9
# CÓDIGO MORSE
# Fecha publicación enunciado: 02/03/22
# Fecha publicación resolución: 07/03/22
# Dificultad: MEDIA
#
# Enunciado: Crea un programa que sea capaz de transformar texto natural a código morse y viceversa.
# - Debe detectar automáticamente de qué tipo se trata y realizar la conversión.
# - En morse se soporta raya "—", punto ".", un espacio " " entre letras o símbolos y dos espacios entre palabras "  ".
# - El alfabeto morse soportado será el mostrado en https://es.wikipedia.org/wiki/Código_morse.
#
# Información adicional:
# - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
# - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
# - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
# - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#
#

import re

# List of caracters
LATIN_CARACTERS = [
    "CH",
    ".",
    ",",
    "?",
    "\"",
    "/",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "Ñ",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
]   
MORSE_CARACTERS = [
    "----",     # "CH",
    ".-.-.-",   # .
    "--..--",   # ,
    "..--..",   # ?
    ".-..-.",   # "
    "-..-.",    # /
    ".-",       # "A",
    "-...",     # "B",
    "-.-.",     # "C",
    "-..",      # "D",
    ".",        # "E",
    "..-.",     # "F",
    "--.",      # "G",
    "....",     # "H",
    "..",       # "I",
    ".---",     # "J",
    "-.-",      # "K",
    ".-..",     # "L",
    "--",       # "M",
    "-.",       # "N",
    "--.--",    # "Ñ",
    "---",      # "O",
    ".--.",     # "P",
    "--.-",     # "Q",
    ".-.",      # "R",
    "...",      # "S",
    "-",        # "T",
    "..-",      # "U",
    "...-",     # "V",
    ".--",      # "W",
    "-..-",     # "X",
    "-.--",     # "Y",
    "--..",     # "Z",
    "-----",    # "0",
    ".----",    # "1",
    "..---",    # "2",
    "...--",    # "3",
    "....-",    # "4",
    ".....",    # "5",
    "-....",    # "6",
    "--...",    # "7",
    "---..",    # "8",
    "----.",    # "9",
]

MORSE_VALIDATION = r"^(\s|\.|-)+$"
LATIN_VALIDATION = r"^([A-Z0-9]|\s|\.|\,|\"|\?|\/)+$"

def morse_encode_decode(text: str)-> str:
    '''
    Convierte un texto a código morse y viceverse

    Recibe por parametro el texto o código morse a convertir

    Retorna el texto convertido
    '''

    # Convertimos texto a mayusculas (Ya que el código Morse no tiene mayusculas o minusculas)
    text = text.upper()

    if re.match(MORSE_VALIDATION, text) is not None:    #Validamos si solo tiene caracteres Morse (solo ".", "-" o espacios " ")
        ORIGIN = MORSE_CARACTERS
        DEST = LATIN_CARACTERS
        text = text.replace("  ", " SPACE ")            #Evitamos perder los espacios en la conversión
        text_list = text.split()
        text_index = 0
        for morse_caracter in text_list:
            if morse_caracter in ORIGIN:
                origin_index = ORIGIN.index(morse_caracter)
                text_list[text_index] = DEST[origin_index]
                text_index += 1
            elif morse_caracter == "SPACE":
                text_list[text_index] = " "             
                text_index += 1
        
        text = "".join(text_list)
                
    elif re.match(LATIN_VALIDATION, text) is not None:  #Validamos si sólo contiene caracteres permitidos en código Morse (desde A a Z, numeros, coma, punto, espacio, ?, / o ")
        
        for origin_caracter, dest_caracter in zip(LATIN_CARACTERS, MORSE_CARACTERS):
            text = text.replace(origin_caracter, dest_caracter + " ")

    else:
        raise Exception("Invalid caracters in string")

    return text.strip()
