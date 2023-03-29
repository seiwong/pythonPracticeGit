#Calculadora cientifica
class Calculadora:
    def __init__(self,numero) -> None:
        self.numero = numero
        self.datos = [0 for i in range (numero)]        
    def ingresarDato(self):
        self.datos = [int(input("Digite datos "+ str(i+1) + " = ")) for i in range(self.numero)]

class opBasicas(Calculadora):
    def __init__(self) -> None:
        Calculadora.__init__(self,2)

    def suma(self):
        a,b = self.datos
        sum = a+b
        print(f"el resultado de la suma es: {sum}") 
    
    def resta(self):
        a,b= self.datos
        rest = a-b
        print(f"el resultado de la resta es: {rest}")

class raiz(Calculadora):
    def __init__(self) -> None:
        Calculadora.__init__(self,1)
    
    def cuadrada(self):
        a, = self.datos
        import math
        print(f"el resultado de la raiz cuadrada de {self.datos} es: {math.sqrt(a)}")

class opDiferentes(Calculadora):
    def __init__(self) -> None:
        Calculadora.__init__(self,2)
    
    def multiplica(self):
        a,b =self.datos
        multiplica=(a*b)
        print(f"la multiplicacion es {multiplica}")

class Especial(Calculadora):
    def __init__(self) -> None:
        Calculadora.__init__(self,1)

    def factorial(self):
        a, = self.datos
        import math
        print(f"el factorial {a} de 10 es {math.factorial(a)}")

class Divisiones(Calculadora):
    def __init__(self) -> None:
        Calculadora.__init__(self,2)

    def divisionEntera(self):
        a,b = self.datos
        divEntera = a//b
        print(f"la division entera es {divEntera}")

    def divisionNormal(self):
        a,b = self.datos
        divNormal = a/b
        print(f"el resultado de la division es {divNormal}")
    
    def residuo(self):
        a,b=self.datos
        residuo = a%b
        print(f"el residuo de la operacion es {residuo}")

objeto = opBasicas()
objeto = raiz()
#print(isinstance(objeto,raiz))

print(dir(objeto))

print("movida de branch");


