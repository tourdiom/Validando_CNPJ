import re

# Numeros para o cálculo
regressivo = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]

#função para remover os caracteres do cnpj
def remo_caract(cnpj):
    return re.sub(r'[^0-9]', '', cnpj)

#função para multiplicar os 12 primeiros digitos do CNPJ, e verificando os dois ultimos digitos
def mutiplica(cnpj, digito):
    if digito == 1:
        regre = regressivo[1:]
        novo_cnpj = cnpj[:-2]
    elif digito == 2:
        regre = regressivo
        novo_cnpj = cnpj
    else:
        return None
    total = 0

    for indice, regressivos in enumerate(regre):
        total += int(cnpj[indice]) * regressivos

    digito = 11 - (total % 11)
    digito = digito if digito <= 9 else 0

    return f'{novo_cnpj}{digito}'

#função para verificar se é uma sequencia e validar se o CNPJ é valido ou não
def valida(cnpj):
    cnpj = remo_caract(cnpj)
    try:
        if sequencia(cnpj):
            print('É uma sequencia portanto, não é um CNPJ Válido')
            return False
    except:
        return False
    try:
        novo_cnpj = mutiplica(cnpj=cnpj, digito=1)
        novo_cnpj = mutiplica(cnpj=novo_cnpj, digito=2)
    except Exception as e:
        return False


    if novo_cnpj == cnpj:
        return True
    else:
        return False



# print(cnpj)

# Função para evitar a sequencia.
def sequencia(cnpj):
    sequencia = cnpj[0] * len(cnpj)
    if sequencia == cnpj:
        return True
    else:
        return False
