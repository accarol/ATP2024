def menu():
    menu = """
(1) Criar uma turma
(2) Inserir um aluno na turma
(3) Listar a turma
(4) Consultar um aluno por id
(5) Guardar a turma em ficheiro
(6) Carregar uma turma de um ficheiro
(0) Sair da aplicação
"""
    print(menu)
    return

def criar_turma():
    turma = []
    print("A turma foi criada com sucesso.")
    return turma

def inserir_aluno(turma):
    if len(turma) == 5:
        print("Não pode adicionar mais alunos turma. A turma chegou ao limite de 5 alunos.")
    else:
        nome = input("Nome do aluno:")
        id = int(input("ID do aluno:"))
        notaTPC = float(input("Nota do TPC:"))
        notaProj = float(input("Nota do projeto:"))
        notaTeste = float(input("Nota do teste:"))
        notas = [notaTPC, notaProj, notaTeste]
        aluno = (nome, id, notas)
        turma.append(aluno)

def listar_turma(turma):
    if len(turma) == 0:
        print("A turma não tem nenhum aluno.")
    else:
        for aluno in turma:
            print(f"Nome:{aluno[0]}, ID:{aluno[1]}, Notas:{aluno[2]}")

def consultar_aluno(turma):
    procura = int(input("Qual o ID do aluno que quer procurar?"))
    encontrado = False
    for aluno in turma:
        if procura == aluno[1]:
            print(f"Nome:{aluno[0]}, ID:{aluno[1]}, Notas:{aluno[2]}")
            encontrado = True
    if not encontrado:
        print("Aluno não encontrado.")

def linha(aluno):
    res = str(aluno[0]) + ',' + str(aluno[1])
    res = res + '::' + str(aluno[2][0]) + ',' + str(aluno[2][1]) + ',' + str(aluno[2][2])
    res = res + "\n"
    return res

def guardar_turma(turma, fnome):
    file = open(fnome, 'w')
    for aluno in turma:
        file.write(linha(aluno))
    file.close()
    print(f"Turma guardada no ficheiro {fnome}")

def carregar_turma(fnome): #corrigir função!!!!
    turma = []
    f = open(fnome)
    for linha in f:
        campos = linha.split("::")
        nome = campos[0] 
        id = campos[1]
        notas = campos[2]
        notaTPC = float(notas[0])
        notaProj = float(notas[1])
        notaTeste = float(notas[2])
        aluno = (nome, id, notaTPC, notaProj, notaTeste)
        turma.append(aluno)
    f.close()
    return turma

turma = []
menu()
op = input("Introduza uma opção.")
while op != '0':
    if op == '1':
        turma = criar_turma()
    elif op == '2':
        inserir_aluno(turma)
    elif op == '3':
        listar_turma(turma)
    elif op == '4':
        consultar_aluno(turma)
    elif op == '5':
        ficheiro = input("Introduza o nome do ficheiro para guardar.")
        guardar_turma(turma, ficheiro)
    elif op == '6':
        ficheiro = input("Introduza o nome do ficheiro para carregar a turma.")
        carregar_turma(ficheiro)
    else:
        print(f"Opção não encontrada: {op}")
    menu()
    op = input("Introduza uma opção.")
print("Obrigada, volte sempre!")
