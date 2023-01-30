
#
# Reto #4
# ÁREA DE UN POLÍGONO
# Fecha publicación enunciado: 24/01/22
# Fecha publicación resolución: 31/01/22
# Dificultad: FÁCIL
#
# Enunciado: Crea UNA ÚNICA FUNCIÓN (importante que sólo sea una) que sea capaz de calcular y retornar el área de un polígono.
# - La función recibirá por parámetro sólo UN polígono a la vez.
# - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
# - Imprime el cálculo del área de un polígono de cada tipo.
#
# Información adicional:
# - Usa el canal de nuestro discord (https://mouredev.com/discord) "🔁reto-semanal" para preguntas, dudas o prestar ayuda a la acomunidad.
# - Puedes hacer un Fork del repo y una Pull Request al repo original para que veamos tu solución aportada.
# - Revisaré el ejercicio en directo desde Twitch el lunes siguiente al de su publicación.
# - Subiré una posible solución al ejercicio el lunes siguiente al de su publicación.
#
#

class Poligon():

    def __init__(self) -> None:
        pass

    def calcular_perimetro(self) -> None:
        pass


class Triangulo(Poligon):

    def __init__(self, base: float, altura: float) -> None:
        super().__init__()
        self.base = base
        self.altura = altura

class Cuadrado(Poligon):

    def __init__(self, lado: float) -> None:
        super().__init__()
        self.lado = lado

class Rectangulo(Poligon):

    def __init__(self, largo: float, ancho:float) -> None:
        super().__init__()
        self.largo = largo
        self.ancho = ancho

def calcular_area(object: any):
    '''
    Función que calcula el area 
    En este caso sería ideal que cada clase tenga su metodo para calcular el area, 
    pero se realiza de esta manera para cumplir con el enunciado
    '''

    if object.__class__ == Triangulo:
        area = object.base * object.altura / 2
        return area
    elif object.__class__ == Cuadrado:
        area = object.lado * object.lado
        return area
    elif object.__class__ == Rectangulo:
        area = object.largo * object.ancho
        return area
    else:
        print("No se puede calcular perimetro de ese objeto")
        return False


poligono_uno = Triangulo(10, 5)
poligono_dos = Cuadrado(50)
poligono_tres = Rectangulo(10, 20)

print(calcular_area(poligono_uno))
print(calcular_area(poligono_dos))
print(calcular_area(poligono_tres))
print(calcular_area("Poligono"))


