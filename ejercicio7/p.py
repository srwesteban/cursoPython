

class Vehiculo:
    Color = None
    Ruedas = None
    Puertas = None

class Coche(Vehiculo):
    Velocidad = None
    Cilindradas = None

    def __init__(self,color,ruedas, puertas, velocidad,cilindaje):
        self.Color = color
        self.Ruedas = ruedas
        self.Puertas = puertas
        self.Velocidad = velocidad
        self.Cilindradas = cilindaje

    def __str__(self):
        return f" color: {self.Color} ruedas: {self.Ruedas} puertas: {self.Puertas} velocidad: {self.Velocidad} cilindraje: {self.Cilindradas}"


miCoche = Coche("rojo",4,5,"100km",2.0)

print(miCoche)