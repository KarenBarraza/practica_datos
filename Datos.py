#se crea la clase Datos
class Datos:
    #se crea el constructor de la clase
    def __init__(self):
        pass
    #se crean el atributo nombre de la clase con sus respectivos metodos get y set
    @property
    def nombre(self)->str:
        return self._nombre

    @nombre.setter
    def nombre(self, nombre:str):
        self._nombre=nombre
    
    #se crean el atributo apellido de la clase con sus respectivos metodos get y set
    @property
    def apellido(self)->str:
        return self._apellido

    @apellido.setter
    def apellido(self, apellido:str):
        self._apellido=apellido
    
    #se crean el atributo edad de la clase con sus respectivos metodos get y set
    @property
    def edad(self)->int:
        return self._edad

    @edad.setter
    def edad(self, edad:int):
        self._edad=edad
        
    #se crean el atributo correo de la clase con sus respectivos metodos get y set
    @property
    def correo(self)->str:
        return self._correo

    @correo.setter
    def correo(self, correo:str):
        self._correo=correo

    #se crean el atributo cedula de la clase con sus respectivos metodos get y set
    @property
    def cedula(self)->int:
        return self._cedula

    @cedula.setter
    def cedula(self, cedula:int):
        self._cedula=cedula
    
