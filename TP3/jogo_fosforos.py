modo = int(input("Bem vindo(a)! Quem começa a jogar: 1. Utilizador ou 2. Computador?"))
while modo != 1 and modo != 2:
        print("Modo inválido.")
        modo = int(input("Bem vindo(a)! Quem começa a jogar: 1. Utilizador ou 2. Computador?"))
fosforos = 21
import random
if modo == 1:
    while fosforos > 1:
        jogada_utilizador = int(input(f"Há {fosforos} fósforos. Quantos deseja retirar? (1-4)"))
        while jogada_utilizador < 1 or jogada_utilizador > 4 or jogada_utilizador > fosforos:
            jogada_utilizador = int(input(f"Jogada inválida! Há {fosforos} fósforos. Quantos deseja retirar? (1-4)"))
        fosforos = fosforos - jogada_utilizador
        if fosforos == 1:
            print("Sobrou 1 fósforo.")
            print("O computador perdeu!")
        jogada_computador = (fosforos - 1) % 5
        if jogada_computador < 1 or jogada_computador > 4:
            jogada_computador = random.randint(1,4)
        print(f"O computador retirou {jogada_computador} fósforo(s).")
        fosforos = fosforos - jogada_computador
        if fosforos == 1:
            jogada_utilizador = int(input(f"Há {fosforos} fósforos. Quantos deseja retirar? (1-4)"))
            print("Você perdeu!!")
elif modo == 2:
    while fosforos > 1:
        jogada_computador = random.randint(1,4)
        print(f"O computador retirou {jogada_computador} fósforo(s).")
        fosforos = fosforos - jogada_computador
        if fosforos == 1:
            jogada_utilizador = int(input(f"Há {fosforos} fósforos. Quantos deseja retirar? (1-4)"))
            print("Você perdeu!!")
        jogada_utilizador = int(input(f"Há {fosforos} fósforos. Quantos deseja retirar? (1-4)"))
        while jogada_utilizador < 1 or jogada_utilizador > 4 or jogada_utilizador > fosforos:
            jogada_utilizador = int(input(f"Jogada inválida! Há {fosforos} fósforos. Quantos deseja retirar? (1-4)"))
        fosforos = fosforos - jogada_utilizador
        if fosforos == 1:
            print("Sobrou 1 fósforo.")
            print("O computador perdeu!")
