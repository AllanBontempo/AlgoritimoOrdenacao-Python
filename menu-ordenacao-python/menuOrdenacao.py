from ordenacoes import ordenacaoBubble
from ordenacoes import ordenacaoSelection
from ordenacoes import ordenacaoInsertion
import random

def main():
    array = []

    print("\n\n*************************************")
    print("Seja bem vindo ao menu de Ordenação!")
    print("*************************************\n\n")

    quantidade = int(input("Digite a quantidade: "))

    resposta = input("Você deseja os números de maneira randomizada? Responda 'sim' ou 'nao'\n")
    resposta = resposta.lower()
    resposta = resposta.strip()

    if resposta == "sim":
        for tentativa in range(0, quantidade):
            array.append(random.randrange(0, 1000))
    else:
        for tentativa in range(0, quantidade):
            array.append(int(input("Digite um número\n")))


    print("\n")
    print("Escolha o método de ordenação da sua escolha: \n\n 1. Bubble Sort \n\
 2. Selection Sort \n 3. Insertion Sort")

    metodoOrdenacao = int(input("Digite 1, 2 ou 3 e escolha seu método: "))

    print("\n\n")
    print("Array antes da ordenação: {}".format(array))
    print("\n")

    ordenacao = input("Deseja crecente ou decrescente? Digite 'C' ou 'D'\n")
    ordenacao = ordenacao.lower()

    if metodoOrdenacao == 1:
        print("\nOrdenando em Bubble Sort...")
        ordenacaoBubble.ordenar(array, ordenacao)
        if retornarAoMenu() == "sim":
            main()
            print("\n")
    elif metodoOrdenacao == 2:
        print("\nOrdenando em Selection Sort...")
        ordenacaoSelection.ordenar(array, ordenacao)
        if retornarAoMenu() == "sim":
            main()
            print("\n")
    elif metodoOrdenacao == 3:
        print("\nOrdenando em Insertion Sort...")
        ordenacaoInsertion.ordenar(array, ordenacao)
        if retornarAoMenu() == "sim":
            main()
            print("\n")
    else:
        print("Esse método não foi encontrado")
            
def retornarAoMenu():
    return input("Deseja retornar ao menu? Digite sim para voltar \n").lower()

if __name__ == "__main__":
    main()

