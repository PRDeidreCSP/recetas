from datetime import date
from plato import Plato
from ingrediente import Ingrediente

# -----------------------------
# Utilización de clases y objetos: clase MenuSemanal
# Atributos privados: _semana, _ano, _platos
# Métodos públicos: engadir_plato, eliminar_plato, buscar_por_semana, buscar_por_ingrediente
# Dunder methods: __str__ para mostrar resumen del menú
# -----------------------------
class MenuSemanal:
    def __init__(self, semana: int, ano: int):
        self._semana = semana
        self._ano = ano
        self._platos = []

    @property
    def semana(self):
        return self._semana

    @property
    def ano(self):
        return self._ano

    @property
    def platos(self):
        return self._platos

    def engadir_plato(self, plato: Plato):
        self._platos.append(plato)

    def eliminar_plato(self, plato: Plato):
        if plato in self._platos:
            self._platos.remove(plato)

    def buscar_por_semana(self, semana: int):
        return [p for p in self._platos if p.data.isocalendar()[1] == semana]

    def buscar_por_ingrediente(self, nombre: str):
        resultado = []
        for plato in self._platos:
            for ing in plato.ingredientes:
                if ing.nombre.lower() == nombre.lower():
                    resultado.append(plato)
                    break
        return resultado

    def __str__(self):
        return f"Menú Semana {self._semana}, {self._ano} ({len(self._platos)} platos)"