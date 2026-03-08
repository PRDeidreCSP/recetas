from datetime import date 
#from tipo_comida import TipoComida
#from ingrediente import Ingrediente
from recetas.tipo_comida import TipoComida
from recetas.ingrediente import Ingrediente

#nombre clase

class Plato:
    def __init__(self,nome:str , data:date, tipo:TipoComida, tempada:str, preparacion:str, foto:str):
        self._nome = nome
        self._data = data
        self._tipo = tipo
        self._tempada = tempada
        self._preparacion = preparacion
        self._foto = foto
        self._ingredientes = []

    @property
    def nome(self):
        return self._nome

    @property
    def data(self):
        return self._data

    @property
    def tipo(self):
        return self._tipo

    @property
    def ingredientes(self):
        return self._ingredientes

    def engadir_ingrediente(self, ing: Ingrediente):
        self._ingredientes.append(ing)

    def eliminar_ingrediente(self, ing: Ingrediente):
        if ing in self._ingredientes:
            self._ingredientes.remove(ing)

    def mostrar_preparacion(self) -> str:
        return self._preparacion


#dunder methods
    def __str__(self):
        return f"{self._nome} ({self._tipo.value}) - {len(self._ingredientes)} ingredientes"
        