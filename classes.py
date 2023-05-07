class viajero:
    __numero = ''
    __dni = ''
    __nombre = ''
    __apellido = ''
    __millas = ''
    def __init__(self,num,dni,nomb,ape,millas):
        self.__numero = num
        self.__dni = dni
        self.__nombre = nomb
        self.__apellido = ape
        self.__millas = millas
    def __str__ (self):
        return '%s %s %s %s %s' % (self.__numero,self.__dni,self.__nombre,self.__apellido,self.__millas)
    
    def __gt__ (self,otro):
        return self.millas > otro.millas
    def __eq__(self, valor):
        if isinstance(valor, int):
            return self._millas == valor
        elif isinstance(valor, viajero):
            return self._millas == valor._millas
    def __req__(self, valor):
        if isinstance(valor, int):
            return self._millas == valor
        elif isinstance(valor, viajero):
            return self._millas == valor._millas    
    def busqueda (self,numero):
        elem = None
        i = 0
        while i < len(viajero) and not elem:
            if viajero[i].__numero == numero:
                elem = viajero[i]
            else:
                i =+ 1
        return elem
    def __add__(self, millas):
        return viajero(self.numero, self.nombre, self.millas + millas)
    def __sub__(self,millas):
        return viajero(self.numero, self.nombre, self.millas - millas)
    def __radd__(self, millas):
        return viajero(self.numero, self.nombre, self.millas + millas)
    def __rsub__(self,millas):
        return viajero(self.numero, self.nombre, self.millas - millas)