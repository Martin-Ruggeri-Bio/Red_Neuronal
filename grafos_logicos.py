sentencia_or = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

sentencia_and = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 0, 0],
    [1, 1, 1]
]

sentencia_xor = [
    [0, 0, 0],
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]


def grafo_de_sentencia_logica(sentencia_logica):
    if sentencia_logica == 'and':
        return sentencia_and
    elif sentencia_logica == 'or':
        return sentencia_or
    elif sentencia_logica == 'xor':
        return sentencia_xor
    return {}