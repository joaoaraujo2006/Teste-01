import numpy as np

def calculate(list):

    lista = np.array(list).reshape(3,3)

    funcoes = {'mean': np.mean, 'var': np.var, 'std': np.std,'min': np.min,'max': np.max,'sum': np.sum}
    arrays = [0, 1, 2]

    calculations = {}

    for nome, func in funcoes.items():
        mediaGeral = []
        for i in arrays:
            if i <= 1:
                media = func(lista, axis=i).tolist()
            else:
                media = func(lista)
            mediaGeral.append(media)
        calculations[nome] = mediaGeral

    return calculations