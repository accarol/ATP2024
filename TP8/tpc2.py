# a) Especifique uma função que dada uma string e uma substring não vazia, calcula  o número de vezes em que a substring aparece na string, sem que haja sobreposição de substrings:

def strCount(s, subs):
    res = 0
    i = 0
    while i < len(s):
        if s[i:i+len(subs)] == subs:
            res = res + 1
            i = i + len(subs)
        else:
            i = i + 1
    return res

print(strCount("catcowcat", "cat"))
print(strCount("catcowcat", "cow"))
print(strCount("catcowcat", "dog"))

# b) Especifique uma função que recebe uma lista de números inteiros positivos e devolve o menor produto que for possível calcular multiplicando os 3 menores inteiros da lista:

def produtoM3(lista):
    menor1 = lista[0]
    menor2 = lista[1]
    menor3 = lista[2]
    if menor1 > menor2:
        menor1, menor2 = menor2, menor1
    if menor2 > menor3:
        menor2, menor3 = menor3, menor2
    if menor1 > menor2:
        menor1, menor2 = menor2, menor1
    for x in lista[3:]:
        if x < menor1:
            menor3 = menor2
            menor2 = menor1
            menor1 = x
        elif x < menor2:
            menor3 = menor2
            menor2 = x
        elif x < menor3:
            menor3 = x
    mprod = menor1*menor2*menor3
    return mprod

print(produtoM3([12,3,7,10,12,8,9]))

# c) Especifique uma função que dado um número inteiro positivo, repetidamente adiciona os seus dígitos até obter apenas um dígito que é retornado como resultado:

def reduxInt(n):
    while n >= 10:
        sn = str(n)
        soma = 0
        for d in sn:
            soma = soma + int(d)
        n = soma
    soma = n  # para sair só n, se menor que 10
    return soma

print(reduxInt(38))
print(reduxInt(777))
print(reduxInt(5)) # dá erro, então sair só n

# d) Especifique uma função que recebe duas strings, `string1` e `string2`, e devolve o índice da primeira ocorrência de `string2` em `string1`, caso não ocorra nenhuma vez a função deverá retornar `-1`:

def myIndexOf(s1, s2):
    res = -1
    i = 0
    while i < len(s1):
        if s1[i:i+len(s2)] == s2:
            res = i
        i = i + 1
    return res

print(myIndexOf("Hoje está um belo dia de sol!", "belo"))
print(myIndexOf("Hoje está um belo dia de sol!", "chuva"))
