#polimorfismo

'''class Animales:
    def __init__(self,nombre) -> None:
        self.nombre = nombre
    
    def tipoAnimal(self):
        pass

class Leon(Animales):
    def tipoAnimal(self):
        print("animal salvaje")

class Perro(Animales):
    def tipoAnimal(self):
        print("animal domestico")


nuevoAnimal= Leon("Simba")
print(nuevoAnimal.nombre)
nuevoAnimal.tipoAnimal()


nuevoAnimalDos= Perro("Rex")
print(nuevoAnimalDos.nombre)
nuevoAnimalDos.tipoAnimal()

#polimorfismo por funcion

class Tomate:
    def tipo(self):
        print("vegetal")
    
    def color(self):
        print("rojo")

class Manzana:
    def tipo(self):
        print("fruta")

    def color(self):
        print("verde")
    

def funcion(objeto):
    objeto.tipo()
    objeto.color()

nuevoTomate = Tomate()
funcion(nuevoTomate)

nuevaManzana = Manzana()
funcion(nuevaManzana)

#polimorfismo por metodo

class Colombia:
    def capital(self):
        print("Bogota")
    
    def idioma(self):
        print("espaniol")

class Francia:
    def capital(self):
        print("Paris")
    
    def idioma(self):
        print("frances")


colombiano = Colombia()
frances = Francia()

for pais in (colombiano,frances):
    pais.capital()
    pais.idioma()'''

#polimorfismo por herencia

class Aves:
    def volar(self):
        print("la mayoria de las aves pueden volar")

class Aguila(Aves):
    def volar(self):
        print("las aguilas pueden volar")

class Gallina(Aves):
    def volar(self):
        print("las gallinas no vuelan")

objAve = Aves()
objAve.volar()

objAveUno = Aguila()
objAveUno.volar()

objAveDos = Gallina()
objAveDos.volar()