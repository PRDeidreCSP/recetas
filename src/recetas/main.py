# src/recetas/main.py

from recetas.plato import Plato
from recetas.ingrediente import Ingrediente
from recetas.tipo_comida import TipoComida
from datetime import date

# Crear ingredientes
tomate = Ingrediente("Tomate", 2, "unidades")
lechuga = Ingrediente("Lechuga", 1, "unidad")
pollo = Ingrediente("Pollo", 200, "g")

# Crear un plato
ensalada = Plato("Ensalada", date.today(), TipoComida.COMIDA, "Verano", "Mezclar todo", "ensalada.jpg")
ensalada.engadir_ingrediente(tomate)
ensalada.engadir_ingrediente(lechuga)

pollo_asado = Plato("Pollo Asado", date.today(), TipoComida.CENA, "Todo el año", "Hornear 40 min", "pollo.jpg")
pollo_asado.engadir_ingrediente(pollo)

# Mostrar platos
print(ensalada)
print(pollo_asado)

# Mostrar preparación
print(ensalada.mostrar_preparacion())
print(pollo_asado.mostrar_preparacion())