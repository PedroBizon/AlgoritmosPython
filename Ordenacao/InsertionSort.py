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

def InsertionSort(lista):
    for i in range(0, len(lista)):
        if i==0:
            continue
        j = i
        while j > 0:
            if(lista[j] < lista[j-1]):
                troca(lista, j, j-1)
                j -= 1
            else:
                break
    
    return lista

"""
Exemplo:
Entrada: 3, 8, 9, 6, 7, 16, 35, 92, 71, 38, 84, 27
Saída esperada: 3, 6, 7, 8, 9, 16, 27, 35, 38, 71, 84, 92
"""

lista = [3, 8, 9, 6, 7, 16, 35, 92, 71, 38, 84, 27]

print('Lista antes da ordenação: ')
print(lista)

InsertionSort(lista)

print("Lista Ordenada: ")
print(lista)
