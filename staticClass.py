import math

class Pastel:
    def __init__(self,ingredientes,tamanio):
        self.ingredientes = ingredientes
        self.tamanio = tamanio
    
    def __repr__(self) -> str:
        return (f"Pastel({self.ingredientes}, "f"{self.tamanio})")
    
    def area(self):
        return self.tamanio_area(self.tamanio)
    
    @staticmethod
    def tamanio_area(A):
        return A ** 2 * math.pi

nuevoPastel = Pastel(['harina', 'azucar', 'leche', 'crema'],4)

print(f"el area del pastel es: {nuevoPastel.tamanio_area(12)}")

print("probando push");
