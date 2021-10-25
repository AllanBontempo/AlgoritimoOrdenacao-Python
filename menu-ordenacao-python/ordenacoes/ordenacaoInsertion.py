import time

def ordenar(array, ordenacao):
    inicio = time.time()
    for i in range(1, len(array)):
        chave = array[i]
        j = i-1
        if ordenacao == 'c':
            while j >= 0 and chave < array[j]:
                array[j+1] = array[j]
                j -= 1
            array[j+1] = chave
        elif ordenacao == 'd':
            while j >= 0 and chave > array[j]:
                array[j+1] = array[j]
                j -= 1
            array[j+1] = chave

    print(array)
    fim = time.time()
    print("*******************************")
    print("O tempo do Insertion Sort é: {}".format((fim - inicio)))
    print("*******************************\n")
