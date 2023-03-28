#encapsulacion

'''class Cliente:
    def __init__(self) -> None:
        self.__codigo = 4321

    def __cuenta(self):
        print("cuenta procesamiento")

    def getCodigo(self):
        return self.__codigo

persona = Cliente()
#para llamar el valor necesito obj._nombreClase__nombre atributo

print(persona._Cliente__codigo)

persona._Cliente__cuenta()'''

#metodo super()

class Mamifero:
    def __init__(self,nombre) -> None:
        print(nombre,"es un animal de sangre caliente")

class Leon(Mamifero):
    def __init__(self) -> None:
        print("el leon es un animal de cuatro patas")
        super().__init__("simba")


nuevoLeon= Leon()