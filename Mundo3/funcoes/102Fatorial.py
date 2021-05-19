# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
# indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(numero, show=False):
    """
    :param numero:
    :param show: Opcional para mostrar a conta
    :return: Fotorial do número passado
    """
    fat = 1
    for i in range(numero, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        fat *= i
    return fat


numero = int(input('Informe o número: '))
print(fatorial(numero, True))


