def ordenar(array, ordenacao):
    for numeros in array:
        if ordenacao == "c":
            for index, numero in enumerate(array):
                if (index+1 < len(array) and index - 1 >= 0):
                    if array[index-1] > array[index]:
                        auxiliar = array[index-1]
                        array[index-1] = array[index]
                        array[index] = auxiliar
        elif ordenacao == "d":
            for index, numero in enumerate(array):
                if (index+1 < len(array) and index - 1 >= 0):
                    if array[index-1] < array[index]:
                        auxiliar = array[index-1]
                        array[index-1] = array[index]
                        array[index] = auxiliar
    print(array)
