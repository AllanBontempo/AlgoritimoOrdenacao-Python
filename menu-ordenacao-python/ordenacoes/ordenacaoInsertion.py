def ordenar(array, ordenacao):
    for index, numero in enumerate(array):
        j = index + 1
        if ordenacao == "c":
            ordenarCrescente(array, index, j)
        elif ordenacao == "d":
            ordenarDecrescente(array, index, j)

    print(array)


def ordenarCrescente(array, index, j):
    for number in array:
        if j < len(array):
            if array[j] < array[index]:
                auxiliar = array[j]
                array[j] = array[index]
                array[index] = auxiliar
            j = j + 1
    return array


def ordenarDecrescente(array, index, j):
    for number in array:
        if j < len(array):
            if array[j] > array[index]:
                auxiliar = array[j]
                array[j] = array[index]
                array[index] = auxiliar
            j = j + 1
    return array