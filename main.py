import func
while True:
    cnpj1 = input('Digite um CNPJ: ')

    if func.valida(cnpj1):
        print(f'O CNPJ: {cnpj1} é Válido')
    else:
        print(f'O CNPJ {cnpj1} é Inválido')



