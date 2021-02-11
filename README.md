# Lista Circular Duplamente Encadeada Com Cursor

## Descrição

Trabalho de Estrutura de Dados (INE5609) - UFSC,  
por Matheus Franzoni Machado.  

## Estrutura

### Elemento

Classe que representa os elementos os quais, unidos, formarão a Lista.  
Cada elemento possui: um valor próprio, um outro elemento anterior da lista e um outro elemento posterior da lista.  

#### Métodos

- ***valor():*** retorna propriedade _valor_ do Elemento.
- ***proximo():*** retorna propriedade _proximo_ do Elemento, que representa o próximo elemento da lista.
- ***anterior():*** retorna propriedade _anterior_ do Elemento, que representa o elemento anterior da lista.
- ***proximo(elemento):*** _setter_ da propriedade _proximo_.
- ***anterior(elemento):*** _setter_ da propriedade _anterior_.
  
### Lista

Classe que representa a lista a qual será formada pela união dos elementos.  
Cada lista possui: um indicador do seu início, um indicador do seu final e um cursor, para navegar por ela.  

#### Métodos

- ***tamanho():*** retorna propriedade _tamanho_ da Lista, que representa o tamanho atual da lista.
- ***inicio():*** retorna propriedade _inicio_ da Lista, que representa o elemento inicial da lista.
- ***fim():*** retorna propriedade _fim_ da Lista, que representa o elemento final da lista.
- ***atual():*** retorna propriedade _atual_ da Lista, que representa o elemento atual da lista (que está sendo "apontado").
- ***limite():*** retorna propriedade _limite_ da Lista, que representa o limite da lista.
- ***inicio(elemento):*** _setter_ da propriedade _inicio_.
- ***fim(elemento):*** _setter_ da propriedade _fim_.
- ***atual(elemento):*** _setter_ da propriedade _atual_.
- ***vazia():*** retorna valor do tipo _boolean_, que representa se a lista está vazia.
- ***cheia():*** retorna valor do tipo _boolean_, que representa se a lista está cheia.
- ***buscar_elemento(elemento):*** retorna valor do tipo _Elemento_ se o elemento passado como parâmetro estiver na lista, caso contrário None.
- ***contem(elemento):*** retorna boolean, se o elemento passado como parâetro estiver na lista.
- ***posicao_de(elemento):*** retorna valor do tipo _number_ referente à posição do elemento passado como parâmetro, se o elemento não estiver na lista, retornará -1.
- ***ir_para_primeiro():*** move o _cursor_ para o inicio da lista.
- ***ir_para_ultimo():*** move o _cursor_ para o fim da lista.
- ***avancar_n_posicoes(n):*** move o _cursor n_ vezes para frente.
- ***retroceder_n_posicoes(n):***  move o _cursor n_ vezes para trás.
- ***inserir_quando_vazio(elemento):***  insere elemento na lista vazia, função chamada pelas outras funções de inserção caso a lista esteja vazia.
- ***inserir_antes_do_atual(elemento):***  insere elemento no depois do _cursor_ da lista.
- ***inserir_depois_do_atual(elemento):***  insere elemento no antes do _cursor_ da lista.
- ***inserir_na_frente(elemento):***  insere elemento no início da lista.
- ***inserir_no_fim(elemento):***  insere elemento no fim da lista.
- ***inserir_na_posicao(n, elemento):***  insere elemento na posição passada como parâmetro.
- ***excluir_todos():*** esvazia a lista, função chamada pelas outras funções de exclusão caso haja apenas um elemento na lista.
- ***excluir_atual():*** exclui o elemento atual (_cursor_).
- ***excluir_primeiro():*** exclui início da lista (primeiro elemento).
- ***excluir_ultimo():*** exclui fim da lista (último elemento).
- ***excluir_elemento(elemento):*** exclui o elemento passado como parâmetro.
- ***excluir_da_posicao(n):*** exclui o elemento da posição passada como parâmetro.
