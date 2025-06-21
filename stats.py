def conteopalabras(contenido):
    palabras = contenido.split()
    return len(palabras)


def conteocar(contenido):
    texto = contenido.lower()
    dic = {}
    for i in texto:
        if i in dic.keys():
            dic[i] = dic[i]+1
        else:
            dic[i] = 1
    return dic


def transformar(diccionario):
    lista = []

    for i in diccionario.keys():
        dic = {}
        dic["char"] = i
        dic["num"] = diccionario[i]
        lista.append(dic)
    return lista


def sort_on(items):
    return items["num"]


def ordenar(diccionario):
    trans = transformar(diccionario)
    trans.sort(reverse=True, key=sort_on)
    return trans
