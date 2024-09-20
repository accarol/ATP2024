import random
numero = random.randint(0, 100)
a = int(input("Diga um número entre 0 e 100."))
tentativas = 1

while a != numero:
    if a > numero:
        print("O número que pensei é menor.")
        a = int(input("Diga um número entre 0 e 100."))
        tentativas = tentativas + 1
    else:
        print("O número que pensei é maior.")
        a = int(input("Diga um número entre 0 e 100."))
        tentativas = tentativas + 1
print("Acertou!")
print(f"Número de tentativas: {tentativas}")
