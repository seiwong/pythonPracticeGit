class Estudiante:
    def __init__(self,nombre,apellido,edad) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __repr__(self) -> str:
        return f"Hola soy {self.nombre} {self.apellido} y tengo {self.edad}"
    
nuevoEstudiante= Estudiante("Victor", "Cruz", 17)

print(f"{nuevoEstudiante !r} ")