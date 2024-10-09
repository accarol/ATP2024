import random

def criarlista(N):
    N = int(input("Quantos números aleatórios deseja gerar?"))
    lista = [random.randint(1, 100) for x in range(N)]
    return lista

def userLista(N):
    N = int(input("Quantos números deseja introduzir? "))
    i = 1
    while i <= N:
        x = int(input(f"Introduza o número {i}/{N}."))
        lista.append(x)
        i = i + 1
    return lista

def somaLista(lista):
    res = 0
    for x in lista:
        res = res + x
    return res

def mediaLista(lista):
    res = 0
    i = 0
    while i < len(lista):
        res = res + lista[i]
        i = i + 1
    media = res / len(lista)
    return media

def maiorLista(lista):
    res = lista[0]
    for x in lista:
        if x > res:
            res = x
    return res

def menorLista(lista):
    res = lista[0]
    for x in lista:
        if x < res:
            res = x
    return res

def estaOrdenadaC(lista):
    res = True
    i = 0 
    while res and i < len(lista)-1:
        if lista[i] > lista[i+1]:
            res = False
        else:
            i = i + 1
    return res

def estaOrdenadaDC(lista):
    res = True
    i = 0
    while res and i < len(lista)-1:
        if lista[i] < lista [i+1]:
            res = False
        else:
            i = i + 1
    return res

def procurarElemento(lista):
    n = int(input("Introduza o elemento que deseja procurar."))
    i = 0
    res = -1
    while i < len(lista):
        if n == lista[i]:
            res = i
        i = i + 1
    return res

def menu():
    print("Menu:")
    print("1) Criar Lista")
    print("2) Ler Lista")
    print("3) Soma")
    print("4) Média")
    print("5) Maior")
    print("6) Menor")
    print("7) Ordenada por ordem crescente")
    print("8) Ordenada por ordem decrescente")
    print("9) Procura um elemento")
    print("0) Sair")

lista = []

menu()
opção = input("Selecione a opção desejada:")

while opção != '0':
    if opção == '1':
        lista = criarlista(lista)
        print("Lista criada:", lista)
    elif opção == '2':
        lista = []
        userLista(lista)
        print("Lista atualizada:", lista)
    elif opção == '3':
        somaLista(lista)
        print("A soma é:", somaLista(lista))
    elif opção == '4':
        mediaLista(lista)
        print("A média é:", mediaLista(lista))
    elif opção == '5':
        maiorLista(lista)
        print("O maior elemento é:", maiorLista(lista))
    elif opção == '6':
        menorLista(lista)
        print("O menor elemento é:", menorLista(lista))
    elif opção == '7':
        if estaOrdenadaC(lista):
            print("Sim")
        else:
            print("Não")
    elif opção == '8':
        if estaOrdenadaDC(lista):
            print("Sim")
        else:
            print("Não")
    elif opção == '9':
        print(procurarElemento(lista))
    else:
        print("Opção inválida.")
    menu()
    opção = input("Selecione a opção desejada:")
print("Esta é a lista guardada:", lista)
print("Adeus, volte sempre!")
