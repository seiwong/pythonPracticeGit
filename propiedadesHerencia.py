#propiedades

class Empleado:
    def __init__(self,nombre,salario) -> None:
        self.__nombre = nombre
        self.__salario = salario
    
    def __getNombre(self):
        return self.__nombre
    def __getSalario(self):
        return self.__salario
    
    def __setNombre(self, nombre):
        self.__nombre = nombre
    def __setSalario(self,salario):
        self.__salario = salario
    
    def __delNombre(self):
        del self.__nombre
    def __delSalario(self):
        del self.__salario

    nombre = property (fget= __getNombre,
                        fset= __setNombre,
                        fdel= __delNombre,
                        doc= "soy la propiedad del 'nombre'")

    salario=property(fget= __getSalario)

empleadoUno = Empleado("Victor", 3000)
empleadoUno.nombre = "Sara"
print(empleadoUno.nombre, empleadoUno.salario)
help(empleadoUno)

print("probando push");
