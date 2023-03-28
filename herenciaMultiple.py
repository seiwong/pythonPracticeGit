class Telefono:
    def __init__(self) -> None:
        pass

    def llamar(self):
        print("llamando...")
    
    def ocupado(self):
        print("ocupado....")

class Camara:
    def __init__(self):
        pass

    def tomarFoto():
        print("tomando foto...")

class Reproduccion:
    def __init__(self):
        pass

    def reproduccion():
        print("reproduciendo musica...")

    def reproducirVideo():
        print("reproducir video...")

class Smartphone(Telefono,Camara,Reproduccion):
    def __del__(self):
        print("telefono apagado")

movil = Smartphone()

print(movil.tomarFoto())