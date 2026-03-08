class Ingrediente:
    def __init__(self, nome:str, cantidade:float , unidade:str):
        self.__nome = nome
        self.__cantidade = cantidade
        self.__unidade = unidade 

    @property   #acceso solo lectura
    def nome(self):
        return self.__nome    
    
    @property     #acceso solo lectura
    def cantidade(self):
        return self.__cantidade 

    @cantidade.setter #para poder escribir 
    def cantidade(self,nova_cantidade: float):
            if nova_cantidade< 0:
                raise ValueError("A cantidade debe ser maior que cero")
            self.cantidade =nova_cantidade
    
    @property #acceso solo lectura 
    def unidade(self):
        return self.__unidade
    

    def __str__(self):
        return f"{self.nome}: {self.cantidade} {self.unidade}"
