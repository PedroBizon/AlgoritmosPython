"""

Implementação simples do algoritmo Bubble Sort.

Sua complexidade de processamento é de n^2, sendo que ele não precisa de memória 
extra para executar.

O algoritmo recebe uma lista e retorna ela mesma, porém em ordem crescente.

"""

def troca(lista, indice1, indice2):

    """
    Função auxiliar que troca de posição os elementos das posições indice1 e indice2
    em uma lista 
    """

    aux = lista[indice1]
    lista[indice1] = lista[indice2]
    lista[indice2] = aux

def BubbleSort(lista):
    for i in range(0, len(lista)-1):
        if(lista[i] > lista[i+1]): 
            troca(lista, i, i+1)
            j=i
            while j>=1:
                if(lista[j-1] > lista[j]):
                    troca(lista, j-1, j)
                    j -= 1
                else:
                    break
    
    return lista
    
        
"""
Exemplo:
Entrada: 9, 8, 7, 6, 5, 4, 3, 2, 1
Saída esperada: 3, 6, 7, 8, 9, 16, 27, 35, 38, 71, 84, 92
"""

lista = [9, 8, 7, 6, 5, 4, 3, 2, 1]

print('Lista antes da ordenação: ')
print(lista)

BubbleSort(lista)

print("Lista Ordenada: ")
print(lista)
