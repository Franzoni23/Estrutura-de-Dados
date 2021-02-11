class Elemento:
    
    def __init__(self, valor: int):
        self.__valor = valor
        self.__proximo = None
        self.__anterior = None

    @property
    def valor(self):
        return self.__valor

    @property
    def proximo(self):
        return self.__proximo

    @property
    def anterior(self,):
        return self.__anterior

    @proximo.setter
    def proximo(self, proximo):
        self.__proximo = proximo

    @anterior.setter
    def anterior(self, anterior):
        self.__anterior = anterior