#se importa la clase Datos y List de typing
from Datos import Datos
from typing import List
#se crea la clase GestionDatos
class GestionDatos:
    #se crea el constructor de la clase y se inicializa la lista vacia
    def __init__(self):
        self._lista =[]
    
    @property
    def lista(self)->List:
        return self._lista

    @lista.setter
    def lista(self, lista:List):
        self._lista=lista
    
    #se crea el metodo para agregar datos a la lista
    def agregar_datos(self, datos:Datos):
        self.lista.append(datos)
        
    #se crea el metodo para consultar datos en la lista
    def consultarDatos(self, cedula:int)->Datos:
        for datos in self.lista:
            if datos.cedula == cedula:
                return datos
        
    