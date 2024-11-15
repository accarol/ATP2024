# a) `quantosPost`, que indica quantos posts estão registados:

def quantosPost(redeSocial):
    return len(redeSocial)

# b) `postsAutor`, que devolve a lista de posts de um determinado autor:

def postsAutor(redeSocial, autor):
    posts_autor = []
    for post in redeSocial:
        if autor == post["autor"]:
            posts_autor.append(post)
    if posts_autor == []:
        return None
    return posts_autor

# c) `autores`, que devolve a lista de autores de posts ordenada alfabeticamente:

def autores(redeSocial):
    lista_autores = []
    for post in redeSocial:
        if post["autor"] not in lista_autores:
            lista_autores.append(post["autor"])
    lista_autores.sort()
    return lista_autores

# d) `insPost`, que acrescenta um novo post à rede social a partir dos parâmetros recebidos e devolve a nova rede social. 

def insPost(redeSocial, conteudo, autor, dataCriacao, comentarios):
    for post in redeSocial:
        nid = int(post["id"][1:])
    npost = {"id":f"p{nid+1}", "conteúdo": conteudo, "autor": autor, "dataCriação": dataCriacao, "comentários": comentarios}
    redeSocial.append(npost)
    return redeSocial

# e) `remPost`, que remove um post da rede, correspondente ao `id` recebido.

def remPost(redeSocial, id):
    encontrado = False
    i = 0
    while not encontrado and i < len(redeSocial):
        if redeSocial[i]["id"] == id:
            encontrado = True
            del redeSocial[i]
        i = i + 1

# f) `postsPorAutor`, que devolve uma distribuição de posts por autor (à semelhança do que foi feito nas aulas).

def postsPorAutor(redeSocial):
    distrib = {}
    for post in redeSocial:
        if post["autor"] not in distrib:
            distrib[post["autor"]] = 1
        else:
            distrib[post["autor"]] = distrib[post["autor"]] + 1
    return distrib

# g) `comentadoPor`, que recebe um autor e devolve a lista de posts comentados por esse autor.

def comentadoPor(redeSocial, autor):
    posts_com = []
    for post in redeSocial:
        for comentario in post["comentários"]:
            if autor == comentario["autor"]:
                posts_com.append(post)
    return posts_com
