help(print)

def contador(inicio, fim, passo):
    """
    :param inicio:
    :param fim:
    :param passo:
    :return o contador entre inicio fim pulando o valor do passo:
    Função criada por Diego Mucheniski em 18/05/2021
    """
    for i in range(inicio, fim, passo):
        print(i)


# Funcão com parametros opcionais, basta colocar o valor recebendo zero, caso não seja passado fica como opcional e não da erro
def somar(a, b, c=0):
    """
    :param a:
    :param b:
    :param c é opcional porque está recebendo zero já:
    :return Soma dos valores passados:
    Criado por Diego Mucheniski 18/05/2021
    """
    soma = a + b + c
    print(f'A soma é {soma}')


def testeEscopo():
    global a
    a = 8
    variavel = 4
    print(f'Variável dentro da função vale {variavel}')
    print(f'Mudei o valor de a global dentro da função, agora vale {a}')


def somarComRetorno(a, b, c):
    soma = a + b + c
    return soma


help(contador)
somar(1, 2, 4)
somar(3, 3)

# Escopo de variavies
variavel = 2
a = 3
print(f'Variável global vale {variavel}')
print(f'a global vale {a}')
testeEscopo()
print(f'a global depois da função vale {a}')


soma1 = somarComRetorno(3, 4, 6)
print(soma1)

