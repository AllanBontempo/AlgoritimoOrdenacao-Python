import time


def ordenar(array, ordenacao):
    inicio = time.time()
    for i in range(len(array)):
        auxiliar = i
        for j in range(i+1, len(array)):
            if ordenacao == 'c':
                if array[auxiliar] > array[j]:
                    auxiliar = j
            elif ordenacao == 'd':
                if array[auxiliar] < array[j]:
                    auxiliar = j
        
        array[i], array[auxiliar] = array[auxiliar], array[i]
    print(array)
    fim = time.time()
    print("*******************************")
    print("O tempo do Selection Sort é: {}".format((fim - inicio)))
    print("*******************************\n")