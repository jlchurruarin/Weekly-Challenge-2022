
#
# Reto #11
# ELIMINANDO CARACTERES
# Fecha publicación enunciado: 14/03/22
# Fecha publicación resolución: 21/03/22
# Dificultad: FÁCIL
#
# Enunciado: Crea una función que reciba dos cadenas como parámetro (str1, str2) e imprima otras dos cadenas como salida (out1, out2).
# - out1 contendrá todos los caracteres presentes en la str1 pero NO estén presentes en str2.
# - out2 contendrá todos los caracteres presentes en la str2 pero NO estén presentes en str1.
#
# Información adicional:
# - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
# - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
# - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
# - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#
#/

def diferencia_de_caracteres(string_one:str, string_two:str):
    '''
    Función que verifica dos strings e imprime los caracteres que estan presentes en uno y en otro no.

    '''

    string_one = string_one.lower()
    string_two = string_two.lower()

    # Omitimos espacios
    string_one_caracters = string_one.replace(" ", "")  
    string_two_caracters = string_two.replace(" ", "")

    for caracter in string_one:
        string_two_caracters = string_two_caracters.replace(caracter,"", 1)
    
    for caracter in string_two:
        string_one_caracters = string_one_caracters.replace(caracter,"", 1)

    print("Caracteres presentes en el primer string, pero no en el segundo: {0}".format(string_two_caracters))
    print("Caracteres presentes en el segundo string, pero no en el primero: {0}".format(string_one_caracters))

diferencia_de_caracteres("Prueba de caracteres", "Lorem ipsum")