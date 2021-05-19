def leiaDinheiro(entrada):
    valido = False
    while not valido:
        valor = str(input(entrada)).replace(',', '.').strip()
        if valor.isalpha() or valor == '':
            print('Erro valor inválido')
        else:
            valido = True
            return float(valor)