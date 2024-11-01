""""
Implemntação do algoritmo de busca binária.

É um algoritmo de busca de complexidade O(log n), porém, apenas funciona em listas ordenadas.

Portanto, caso sua lista não esteja ordenada, é necessário ordená-la para usar a busca binária.
"""

def BuscaBinaria(lista, comecoLista, fimLista, numeroBuscado):
    # Caso de parada
    if(comecoLista == fimLista):
        if(lista[comecoLista] == numeroBuscado):
            return comecoLista
        else:
            # Sinalização de que o elemento buscado não pertence à lista
            return -1
        
    meioLista = (fimLista+comecoLista)//2

    if(lista[meioLista] == numeroBuscado):
        return meioLista

    else:
        if(lista[meioLista] > numeroBuscado):
            return BuscaBinaria(lista, comecoLista, meioLista-1, numeroBuscado)
        else:
            return BuscaBinaria(lista, meioLista+1, fimLista, numeroBuscado)


'''
Segue um teste para a busca binária.

A função BuscaBinaria retorna o índice em que o elemento aparece.

A lista arr tem os núemros de 0 a 16 de forma que o número na lista e o índice dela são iguais para todos os elementos.
'''

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
x = 7

resposta = BuscaBinaria(arr, 0, len(arr)-1, x)

print(resposta)