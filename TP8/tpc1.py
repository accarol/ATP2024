# a) Lista formada pelos elementos que não são comuns às duas listas:

lista1 = [1, 2, 3, 4, 5]
lista2 = [4, 5, 6, 7, 8]  

ncomuns = []
for x in lista1:
    if x not in lista2:
        ncomuns.append(x)
for x in lista2:
    if x not in lista1:
        ncomuns.append(x)

print(ncomuns)

# b) Lista formada pelas palavras do texto compostas por mais de 3 letras:

texto = """Vivia há já não poucos anos algures num concelho do Ribatejo 
    um pequeno lavrador e negociante de gado chamado Manuel Peres Vigário"""

palavras = texto.split()

lista= []
for palavra in palavras:
    if len(palavra) > 3:
        lista.append(palavra)

print(lista)

# c) Lista formada por pares do tipo (índice, valor) com os valores da lista dada:

lista = ['anaconda', 'burro', 'cavalo', 'macaco']

res = []
i = 1
for valor in lista:
    res.append((i,valor))
    i = i + 1

print(res)
