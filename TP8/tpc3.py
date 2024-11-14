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



# e) `remPost`, que remove um post da rede, correspondente ao `id` recebido.



# f) `postsPorAutor`, que devolve uma distribuição de posts por autor (à semelhança do que foi feito nas aulas).



# g) `comentadoPor`, que recebe um autor e devolve a lista de posts comentados por esse autor.

