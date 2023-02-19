
#
# Reto #10
# EXPRESIONES EQUILIBRADAS
# Fecha publicación enunciado: 07/03/22
# Fecha publicación resolución: 14/03/22
# Dificultad: MEDIA
#
# Enunciado: Crea un programa que comprueba si los paréntesis, llaves y corchetes de una expresión están equilibrados.
# - Equilibrado significa que estos delimitadores se abren y cieran en orden y de forma correcta.
# - Paréntesis, llaves y corchetes son igual de prioritarios. No hay uno más importante que otro.
# - Expresión balanceada: { [ a# ( c + d ) ] - 5 }
# - Expresión no balanceada: { a# ( c + d ) ] - 5 }
#
# Información adicional:
# - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la comunidad.
# - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
# - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
# - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#
#/

DELIM = [
        "(", ")",
        "[", "]",
        "{", "}",
        ]

def is_expresion_balanced(expresion: str) -> bool:
    delim_stack = []
    for caracter in expresion:
        if caracter in DELIM:
            delim_stack.append(caracter)

    delim_string = "".join(delim_stack)

    while(len(delim_string) > 0):
        if "()" in delim_string:
            delim_string = delim_string.replace("()", "")
        elif "[]" in delim_string:
            delim_string = delim_string.replace("[]", "")
        elif "{}" in delim_string:
            delim_string = delim_string.replace("{}", "")
        else:
            break
    
    return len(delim_string) == 0


if __name__ == '__main__':
    
    expresion = input("Ingrese la expresión a verificar:\n")

    if is_expresion_balanced(expresion):
        print("La expresión está balanceada")
    else:
        print("La expresión no está balanceada")
