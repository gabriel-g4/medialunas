def crear_diccionario(keys: list, values: tuple) -> dict:
    dic = {}

    if (values != None):
        for i in range(len(keys)):
            dic[keys[i]] = values[i]

    return dic