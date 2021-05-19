def formataValor(valor):
    return f'R${valor}'


def dobroPreco(valor):
    valor *= 2
    return formataValor(valor)


def metadeDoPreco(valor):
    valor = valor / 2
    return formataValor(valor)


def percentual(valor, percentual):
    aux = (valor * (percentual/100)) + valor
    return formataValor(aux)


def resumo(valor, percentual1, percentual2):
    print(f'Valor analisado {formataValor(valor)}')
    print(f'Dobro do preço {dobroPreco(valor)}')
    print(f'Metade do preço {metadeDoPreco(valor)}')
    print(f'{percentual1}% de aumento {percentual(valor, percentual1)}')
    print(f'{percentual2}% de aumento {percentual(valor, percentual2)}')