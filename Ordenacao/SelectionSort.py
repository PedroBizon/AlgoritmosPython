"""

Implementação simples do algoritmo Bubble Sort.

Sua complexidade de processamento é de n^2, sendo que ele não precisa de memória 
extra para executar.

O algoritmo recebe uma lista e retorna ela mesma, porém em ordem crescente.

"""

def troca(lista, indice1, indice2):
    aux = lista[indice1]
    lista[indice1] = lista[indice2]
    lista[indice2] = aux


def SelectionSort(lista, inicio):
    if(inicio == len(lista)-1):
        return lista
    
    for i in range(inicio, len(lista)):
        if(lista[inicio] > lista[i]):
            troca(lista, inicio, i)
    
    inicio += 1
    SelectionSort(lista, inicio)


"""
Exemplo:
Entrada: 3, 8, 9, 6, 7, 16, 35, 92, 71, 38, 84, 27
Saída esperada: 3, 6, 7, 8, 9, 16, 27, 35, 38, 71, 84, 92
"""

lista = [9, 8, 7, 6, 5, 4, 3, 2, 1]

print('Lista antes da ordenação: ')
print(lista)

SelectionSort(lista, 0)

print("Lista Ordenada: ")
print(lista)
