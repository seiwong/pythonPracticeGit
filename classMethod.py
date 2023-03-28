#Metodo de clase
class Pastel:
    def __init__(self,ingredientes) -> None:
        self.ingredientes = ingredientes
    
    def __repr__(self):
        return f"pastel({self.ingredientes !r})"
    
    #metodo de clase
    @classmethod
    def PastelChocolate(cls):
        return cls(['harina', 'leche', 'chocolate'])
    
    @classmethod
    def PastelVainilla(cls):
        return cls(['harina', 'leche', 'vainilla'])
    
print(Pastel.PastelChocolate())