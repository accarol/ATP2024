def inserirSala(cinema,sala):
    res = cinema
    res.append(sala)
    return res

from datetime import date

def listar(cinema):
    print("Filmes em exibição:")
    print("-------------------------")
    for sala in cinema:
        print(f"{sala[2]}")
    today = date.today()
    print("-------------------------")
    print(today)
    return

def listardisponibilidades(cinema):
    print("Lugares disponíveis:")
    print("Filme          Lugares")
    print("-----------------------")
    for sala in cinema:
        print(f"{sala[2]}          {sala[0]-len(sala[1])}")
    today = date.today()
    print("-----------------------")
    print(today)
    return

def procura(cinema,filme):
    res = -1
    i = 0
    while res == -1 and i < len(cinema):
        if cinema[i][2] == filme:
            res = i
        else:
            i = i + 1
    return res

def disponivel(cinema,filme1,lugar):
    res = True
    sala = procura(cinema,filme1)
    if lugar in cinema[sala][1]:
        res = False
    return res

def app_disponivel(cinema):
    for sala in cinema:
        print(sala[2], end=" ")
    salaf = input("Qual o filme que deseja?")
    if salaf == 'Twilight':
        lugar = int(input("Qual o lugar desejado?"))
        if lugar > 0 and lugar <= 150:
            print("Lugar disponível")
        else:
            print("Lugar indisponível")
            salaf = input("Qual o filme que deseja?")
            lugar = int(input("Qual o lugar desejado?"))
    elif salaf == 'Hannibal':
        lugar = int(input("Qual o lugar desejado?"))
        if lugar > 0 and lugar <= 200:
            print("Lugar disponível")
        else:
            print("Lugar indisponível")
            salaf = input("Qual o filme que deseja?")
            lugar = int(input("Qual o lugar desejado?"))
    else:
        print("Filme não em exibição.")
    return disponivel(cinema,salaf,lugar)

def vendebilhete(cinema,filme1,lugar):
    for sala in cinema:
        if sala[2] == filme1:
            sala[1].append(lugar)
    return cinema

def app_disponivel(cinema):
    for sala in cinema:
        print(sala[2], end=" ")
    salaf = input("Qual o filme que deseja? ")
    sala = procura(cinema, salaf)
    if sala == -1:
        print("Filme não em exibição.")
        return False
    lugar = int(input("Qual o lugar desejado? "))
    if 0 < lugar <= cinema[sala][0]:
        lugar_ocupado = lugar in cinema[sala][1]
        if not lugar_ocupado:
            print("Lugar disponível")
            return True
        else:
            print("Lugar indisponível.")
            return False
    else:
        print("Lugar inválido.")
        return False

def menu():
    print("1) Listar filmes")
    print("2) Listar disponibilidade de lugares")
    print("3) Lugar disponível")
    print("4) Vende bilhete")
    print("0) Sair da aplicação")

sala1 = (150, [], "Twilight")
sala2 = (200, [], "Hannibal")
cinema1 = []
cinema1 = inserirSala(cinema1,sala1)
cinema1 = inserirSala(cinema1,sala2)

menu()
op = input("Introduza uma das opções.")
while op != '0':
    if op == '1':
        listar(cinema1)
    elif op == '2':
        listardisponibilidades(cinema1)
    elif op == '3':
        app_disponivel(cinema1)
    elif op == '4':
        filme = input("Qual o filme que deseja? ")
        lugar = int(input("Qual o lugar que deseja? "))
        if disponivel(cinema1, filme, lugar):
            vendebilhete(cinema1, filme, lugar)
            print("Bilhete vendido com sucesso!")
        else:
            print("Não foi possível vender o bilhete.")
    else:
        print("Opção inválida.")
    menu()
    op = input("Introduza uma das opções.")
print("Adeus, volte sempre!")
