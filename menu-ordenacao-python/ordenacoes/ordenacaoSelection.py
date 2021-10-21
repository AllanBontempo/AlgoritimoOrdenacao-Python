def ordenar(array, ordenacao):
    for indice, numeros in enumerate(array):
        if ordenacao == "c":
            array = ordenarCrescente(array, indice)
        elif ordenacao == "d":
            array = ordenarDecrescente(array, indice)
    print(array)


def ordenarCrescente(array, indice):
    for index, numero in enumerate(array):
        if (index+1 < len(array) and index - 1 >= 0):
            if array[index-1] > array[indice-1]:
                auxiliar = array[index-1]
                array[index-1] = array[indice-1]
                array[indice-1] = auxiliar
    return array

def ordenarDecrescente(array, indice):
    for index, numero in enumerate(array):
        if (index+1 < len(array) and index - 1 >= 0):
            if array[index-1] < array[indice-1]:
                auxiliar = array[index-1]
                array[index-1] = array[indice-1]
                array[indice-1] = auxiliar
    return array