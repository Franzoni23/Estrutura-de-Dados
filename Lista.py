from Elemento import Elemento

class Lista:
    
    def __init__(self, limite):
        self.__tamanho = 0
        self.__inicio = None
        self.__fim = None
        self.__atual = None   
        self.__limite = limite 
    
    @property
    def tamanho(self):
        return self.__tamanho

    @property
    def inicio(self):
        return self.__inicio

    @property
    def fim(self):
        return self.__fim

    @property
    def atual(self):
        return self.__atual

    @property
    def limite(self):
        return self.__limite
    
    @inicio.setter
    def inicio(self, elemento):
        self.__inicio = elemento

    @fim.setter
    def fim(self, elemento):
        self.__fim = elemento   

    @atual.setter
    def atual(self, elemento):
        self.__atual = elemento
    
    def lista(self):
        atual = self.inicio
        n = 0
        lista = []
        while n < self.tamanho:
            lista.append(atual.valor)
            atual = atual.proximo
            n = n + 1
        return lista

    def vazia(self):
        return not self.tamanho

    def cheia(self):
        return self.tamanho >= self.limite

    def buscar_elemento(self, elemento):
        if isinstance(elemento, Elemento):
            atual = self.inicio
            n = 0
            reposta = None
            while n < self.tamanho:
                if atual == elemento:
                    resposta = atual
                    break
                atual = atual.proximo
                n = n + 1
            return resposta
        else:
            raise Exception('Parâmetro não é um Elemento')

    def contem(self, elemento):
        if isinstance(elemento, Elemento):
            atual = self.inicio
            n = 0
            resposta = False
            while n < self.tamanho:
                if atual == elemento:
                    resposta = True
                    break
                atual = atual.proximo
                n = n + 1
            return resposta
        else:
            raise Exception('Parâmetro não é um Elemento')
    
    def posicao_de(self, elemento):
        if isinstance(elemento, Elemento):
            atual = self.inicio
            n = 0
            reposta = -1
            while n < self.tamanho:
                if atual == elemento:
                    resposta = n
                    break
                atual = atual.proximo
                n = n + 1
            return resposta
        else:
            raise Exception('Parâmetro não é um Elemento')

    def ir_para_primeiro(self):
        if self.vazia():
            return ('Lista está vazia.')
        else:
            self.__atual = self.inicio
            return ('Cursor está no início.')

    def ir_para_ultimo(self):
        if self.vazia():
            return ('Lista está vazia.')
        else:
            self.__atual = self.fim
            return ('Cursor está no fim.')

    def avancar_n_posicoes(self, n):
        if self.vazia():
            return ('Lista está vazia.')
        else:
            for i in range(n):
                self.__atual = self.atual.proximo
            return 'Cursor avançou ' + str(n) + ' posições'
    
    def retroceder_n_posicoes(self, n):
        if self.vazia():
            return ('Lista está vazia.')
        else:
            for i in range(n):
                self.__atual = self.atual.anterior
            return 'Cursor retrocedeu ' + str(n) + ' posições'
    
    def inserir_quando_vazio(self, elemento):
        if isinstance(elemento, Elemento):
            if self.cheia():
                return ('Lista está cheia.')
            else:
                elemento.__proximo = elemento
                elemento.__anterior = elemento
                self.__inicio = elemento
                self.__fim = elemento
                self.__atual = elemento
                self.__tamanho = 1
                return ('Primeiro elemento inserido.')
        else:
            raise Exception('Parâmetro não é um Elemento')
    
    def inserir_antes_do_atual(self, elemento):
        if isinstance(elemento, Elemento):
            if self.vazia():
                self.inserir_quando_vazio(elemento)
            elif self.cheia():
                return ('A lista está cheia.')
            elif self.contem(elemento):
                return ('Elemento já está na lista.')
            elif self.atual == self.inicio:
                self.inserir_na_frente(elemento)
            else:
                elemento.anterior = self.atual.anterior
                self.__atual.anterior.proximo = elemento
                elemento.proximo = self.atual
                self.__atual.anterior = elemento
                self.retroceder_n_posicoes(1)
                self.__tamanho = self.tamanho + 1
                return ('Elemento inserido antes do atual.')
        else:
            raise Exception('Parâmetro não é um Elemento')

    def inserir_depois_do_atual(self, elemento):
        if isinstance(elemento, Elemento):
            if self.vazia():
                self.inserir_quando_vazio(elemento)
            elif self.cheia():
                return ('A lista está cheia.')
            elif self.contem(elemento):
                return ('Elemento já está na lista.')
            elif self.atual == self.fim:
                self.inserir_no_fim(elemento)
            else:
                elemento.proximo = self.atual.proximo
                self.__atual.proximo.anterior = elemento
                elemento.anterior = self.atual
                self.__atual.proximo = elemento
                self.avancar_n_posicoes(1)
                self.__tamanho = self.tamanho + 1
                return ('Elemento inserido depois do atual.')
        else:
            raise Exception('Parâmetro não é um Elemento')
    
    def inserir_na_frente(self, elemento):
        if isinstance(elemento, Elemento):
            if self.vazia():
                return self.inserir_quando_vazio(elemento)
            elif self.cheia():
                return ('A lista está cheia.')
            elif self.contem(elemento):
                return ('Elemento já está na lista.')
            else:
                elemento.proximo = self.inicio
                self.__inicio.anterior = elemento
                self.__inicio = elemento
                self.__inicio.anterior = self.fim
                self.__fim.proximo = self.inicio
                self.ir_para_primeiro()
                self.__tamanho = self.tamanho + 1
                return ('Elemento inserido no início.')
        else:
            raise Exception('Parâmetro não é um Elemento')
        
    def inserir_no_fim(self, elemento):
        if isinstance(elemento, Elemento):
            if self.vazia():
                self.inserir_quando_vazio(elemento)
            elif self.cheia():
                return ('A lista está cheia')
            elif self.contem(elemento):
                return ('Elemento já está na lista.')
            else:
                elemento.anterior = self.fim
                self.__fim.proximo = elemento
                self.__fim = elemento
                self.__fim.proximo = self.inicio
                self.__inicio.anterior = self.fim
                self.ir_para_ultimo()
                self.__tamanho = self.tamanho + 1
                return ('Elemento inserido no fim.')
        else:
            raise Exception('Parâmetro passado não é um Elemento') 

    def inserir_na_posição(self, n, elemento):
        if isinstance(n, int) and isinstance(elemento, Elemento):
            if self.vazia():
                self.inserir_quando_vazio(elemento)
            elif self.cheia():
                return ('A lista está cheia.')
            elif self.contem(elemento):
                return ('Elemento já está na lista.')
            elif n > self.tamanho:
                return ('Lista vai até a posição' + str(self.tamanho - 1))
            elif n == 0:
                self.inserir_na_frente(elemento)
            else:
                self.ir_para_primeiro()
                self.avancar_n_posicoes(n - 1)
                self.inserir_depois_do_atual(elemento)
        else:
            raise Exception('Parâmetros não são um inteiro e um Elemento')

    def excluir_todos(self):
        if self.vazia():
            raise Exception('A lista está vazia.')
        else:
            self.__inicio = None
            self.__fim = None
            self.__atual = None
            self.__tamanho = 0
            return ('Lista esvaziada.')
    
    def excluir_atual(self):
        if self.vazia():
            return ('A lista está vazia.')
        elif self.atual == self.inicio:
            return self.excluir_primeiro()
        elif self.atual == self.fim:
            return self.excluir_ultimo()
        elif self.tamanho == 1:
            return self.excluir_todos()
        else:
            self.__atual.anterior.proximo = self.atual.proximo
            self.__atual.proximo.anterior = self.atual.anterior
            self.retroceder_n_posicoes(1)
            self.__tamanho = self.tamanho - 1
            return ('Atual excluído.')
    
    def excluir_primeiro(self):
        if self.vazia():
            return ('A lista está vazia.')
        elif self.tamanho == 1:
            return self.excluir_todos()
        else:
            self.__fim.proximo = self.inicio.proximo
            self.__inicio.proximo.anterior = self.fim
            self.__inicio = self.inicio.proximo
            self.ir_para_primeiro()
            self.__tamanho = self.tamanho - 1
            return ('Elemento inicial excluído.')

    def excluir_ultimo(self):
        if self.vazia():
            return ('A lista está vazia.')
        elif self.tamanho == 1:
            self.excluir_todos()
        else:
            self.__fim.anterior.proximo = self.inicio
            self.__inicio.anterior = self.fim.anterior
            self.__fim = self.fim.anterior
            self.ir_para_ultimo()
            self.__tamanho = self.tamanho - 1
            return ('Elemento final excluído.')

    def excluir_elemento(self, elemento):
        if isinstance(elemento, Elemento):
            if self.contem(elemento):
                self.atual = self.buscar_elemento(elemento)
                return self.excluir_atual()
                self.__tamanho = self.tamanho - 1
            else:
                return ('Elemento não está na lista.')
        else:
            raise Exception('Parâmetro não é um Elemento')

    def excluir_da_posicao(self, n):
        if isinstance(n, int):
            if n < self.tamanho:
                self.ir_para_primeiro()
                self.avancar_n_posicoes(n)
                return self.excluir_atual()
            else:
                return ('Posição maior que a lista.')
        else:
            raise Exception('Parâmetro não é um inteiro')   
        
#Dados
l = Lista(5)
e1 = Elemento(1)
e2 = Elemento(2)
e3 = Elemento(3)
e4 = Elemento(4)
e5 = Elemento(5)

#Testes
print('')
print('Lista está vazia?')
print(l.vazia())
print('Tamanho: ' + str(l.tamanho))
print('')
print('Inserindo primeiro elemento')
print(l.inserir_quando_vazio(e1))
print('Início: ' + str(l.inicio.valor))
print('Final: ' + str(l.fim.valor))
print('Cursor: ' + str(l.atual.valor))
print('Tamanho: ' + str(l.tamanho))
print('')
print(l.lista())
print('')
print('Inserindo no início')
print(l.inserir_na_frente(e2))
print('Início: ' + str(l.inicio.valor))
print('Final: ' + str(l.fim.valor))
print('Cursor: ' + str(l.atual.valor))
print('Tamanho: ' + str(l.tamanho))
print('')
print(l.lista())
print('')
print('Inserindo no final')
print(l.inserir_no_fim(e3))
print('Início: ' + str(l.inicio.valor))
print('Final: ' + str(l.fim.valor))
print('Cursor: ' + str(l.atual.valor))
print('Tamanho: ' + str(l.tamanho))
print('')
print(l.lista())
print('')
print('Buscando valor e posição')
print('Valor: ' + str(l.buscar_elemento(e2).valor))
print('Posição: ' + str(l.posicao_de(e2)))
print('')
print(l.lista())
print('')
print('Inserindo antes do atual')
print(l.inserir_antes_do_atual(e4))
print('Início: ' + str(l.inicio.valor))
print('Final: ' + str(l.fim.valor))
print('Cursor: ' + str(l.atual.valor))
print('Tamanho: ' + str(l.tamanho))
print('')
print(l.lista())
print('')
print('Inserindo depois do atual')
print(l.inserir_depois_do_atual(e5))
print('Início: ' + str(l.inicio.valor))
print('Final: ' + str(l.fim.valor))
print('Cursor: ' + str(l.atual.valor))
print('Tamanho: ' + str(l.tamanho))
print('')
print(l.lista())
print('')
print('Lista está cheia?')
print(l.cheia())
print('')
print('Movimentando o cursor')
print(l.avancar_n_posicoes(5))
print('Cursor: ' + str(l.atual.valor))
print(l.retroceder_n_posicoes(2))
print('Cursor: ' + str(l.atual.valor))
print('')
print(l.lista())
print('')
print('Excluindo')
print(l.excluir_elemento(e5))
print('Início: ' + str(l.inicio.valor))
print('Final: ' + str(l.fim.valor))
print('Cursor: ' + str(l.atual.valor))
print('Tamanho: ' + str(l.tamanho))
print('')
print(l.lista())
print('')
print('Excluindo inicial')
print(l.excluir_primeiro())
print('Início: ' + str(l.inicio.valor))
print('Final: ' + str(l.fim.valor))
print('Cursor: ' + str(l.atual.valor))
print('Tamanho: ' + str(l.tamanho))
print('')
print(l.lista())
print('')
print('Excluindo final')
print(l.excluir_ultimo())
print('Início: ' + str(l.inicio.valor))
print('Final: ' + str(l.fim.valor))
print('Cursor: ' + str(l.atual.valor))
print('Tamanho: ' + str(l.tamanho))
print('')
print(l.lista())
print('')
print('Excluindo por posição')
print(l.excluir_da_posicao(0))
print('Início: ' + str(l.inicio.valor))
print('Final: ' + str(l.fim.valor))
print('Cursor: ' + str(l.atual.valor))
print('Tamanho: ' + str(l.tamanho))
print('')
print(l.lista())
print('')
print('Excluindo atual')
print(l.excluir_atual())
print('Início: ' + str(l.inicio))
print('Final: ' + str(l.fim))
print('Cursor: ' + str(l.atual))
print('Tamanho: ' + str(l.tamanho))
print('')
print(l.lista())
print('')