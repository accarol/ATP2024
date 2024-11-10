def menu():
    menu = """
(1) Inserir dados
(2) Listar tabela
(3) Temperaturas médias
(4) Guardar tabela meteorológica em ficheiro
(5) Carregar tabela meteorológica de um ficheiro
(6) Temperatura mínima da tabela
(7) Amplitude térmica
(8) Dia conm o valor máximo de precipitação
(9) Dias com precipitação superior a um limite p
(10) Maior número consecutivo de dias com precipitação abaixo do limite p
(11) Gráficos temperatura min, máx e pluviosidade de uma tabela
(0) Sair
"""
    print(menu)
    return

def criar_tabMeteo():
    tabMeteo = []
    return tabMeteo

def inserir_dados(tabMeteo):
    ano = int(input("Ano:"))
    mês = int(input("Mês:"))
    dia = int(input("Dia:"))
    data = [ano, mês, dia]
    tmin = float(input("Temperatura mínima:"))
    tmax = float(input("Temperatura máxima:"))
    precip = float(input("Precipitação:"))
    dados = (data, tmin, tmax, precip)
    tabMeteo.append(dados)

def listar_tab(tabMeteo):
    if len(tabMeteo) == 0:
        print("A tabela está vazia.")
    else:
        for dados in tabMeteo:
            print(f"{dados[0]},{dados[1]},{dados[2]},{dados[3]}")

def medias(tabMeteo):
    res = []
    for data,tmin,tmax,precip in tabMeteo:
        res.append((data,(tmin+tmax)/2))
    return res

def guardaTabMeteo(t, fnome):
    f = open(fnome, "w")
    for data,tmin,tmax,precip in t:
        linha = f"{data[0]} :: {data[1]} :: {data[2]} :: {tmin} :: {tmax} :: {precip}\n"
        f.write(linha)
    f.close()
    return len(t)

def carregaTabMeteo(fnome):
    res = []
    f1 = open(fnome)
    for linha in f1:
        if linha != "":
            campos = linha.split("::")
            data = (int(campos[0]),int(campos[1]),int(campos[2]))
            res.append((data,float(campos[3]),float(campos[4]),float(campos[5])))
    f1.close()
    return res

def minMin(tabMeteo):
    minima = tabMeteo[0][1]
    for data,tmin,tmax,precip in tabMeteo[1:]:
        if tmin < minima:
            minima = tmin
    return minima

def amplTerm(tabMeteo):
    res = []
    for data,tmin,tmax,precip in tabMeteo:
        res.append((data,tmax-tmin))
    return res 

def maxChuva(tabMeteo):
    max_prec = tabMeteo[0][3]
    max_data = tabMeteo[0][0]
    for data,tmin,tmax,precip in tabMeteo[1:]:
        if precip > max_prec:
            max_prec = precip
            max_data = data
    return (max_data, max_prec)

def diasChuvosos(tabMeteo, p):
    res=[]
    prec = tabMeteo[0][3]
    date = tabMeteo[0][0]
    for data,tmin,tmax,precip in tabMeteo[1:]:
        if precip > p:
            prec = precip
            date = data
            res.append((date,prec))
    return res

def maxPeriodoCalor(tabMeteo, p):
    consecutivos = 0
    contador = 0
    for *_,precip in tabMeteo:
        if precip < p:
            contador = contador + 1
        else:
            if consecutivos < contador:
                consecutivos = contador
            contador = 0
    if consecutivos < contador:
        consecutivos = contador
    return consecutivos

def grafTabMeteo(t): # ainda nao foi feito!!
    
    return

tabMeteo = criar_tabMeteo()
menu()
op = input("Introduza uma opção.")
while op != '0':
    if op == '1':
        inserir_dados(tabMeteo)
    elif op == '2':
        listar_tab(tabMeteo)
    elif op == '3':
        print(medias(tabMeteo))
    elif op == '4':
        ficheiro = input("Introduza o nome do ficheiro para guardar a tabela.")
        guardaTabMeteo(tabMeteo, ficheiro)
    elif op == '5':
        ficheiro = input("Introduza o nome do ficheiro para carregar a tabela.")
        print(carregaTabMeteo(ficheiro)) 
    elif op == '6':
        print(minMin(tabMeteo))
    elif op == '7':
        print(amplTerm(tabMeteo))
    elif op == '8':
        print(maxChuva(tabMeteo))
    elif op == '9':
        limite = float(input("Introduza um valor limite."))
        print(diasChuvosos(tabMeteo, limite))
    elif op == '10':
        limite = float(input("Introduza um valor limite."))
        print(maxPeriodoCalor(tabMeteo, limite))
    elif op == '11':
        grafTabMeteo(tabMeteo)
    else:
        print(f"Opção não encontrada: {op}")
    menu()
    op = input("Introduza uma opção.")
print("Obrigada, volte sempre!")
