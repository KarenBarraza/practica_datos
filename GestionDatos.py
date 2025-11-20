from Datos import Datos
from typing import List
class GestionDatos:
    def __init__(self):
        self._lista =[]
    
    @property
    def lista(self)->List:
        return self._lista

    @lista.setter
    def lista(self, lista:List):
        self._lista=lista

    def agregar_datos(self, datos:Datos)-> Datos:
        self.lista.append(datos)

    def consultarDatos(self, cedula):
        for datos in self.lista:
            if datos.cedula == cedula:
                return datos
        
    # def verlista(self):
    #     if len(self.lista) ==0:
    #         print("No hay personas registradas")
    #     else:
    #         for datos in self.lista:
    #             #print(persosna["nombre"])
    #             print("nombre: ",  self.nombre, "apellido", self.apellido , "edad: ", self.edad, "correo: ", self.correo, "cedula: ", self.cedula)