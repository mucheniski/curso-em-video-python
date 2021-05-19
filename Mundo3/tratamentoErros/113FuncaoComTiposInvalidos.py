# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104,
# incluindo agora a possibilidade da digitação de um número de tipo inválido.
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.


def leiaInt(mensgem):
    while True:
        try:
            numero = int(input(mensgem))
        except ValueError as erro:
            print(f'Deu ruim {erro.__class__}')
            continue
        else:
            return numero


def leiaFloat(mensagem):
    while True:
        try:
            numero = float(input(mensagem))
        except ValueError as erro:
            print(f'Deu ruim {erro.__class__}')
            continue
        except Exception as erro:
            print(f'Deu ruim {erro.__class__}')
            continue
        else:
            return numero


# numeroInteiro = leiaInt('Digite um número int: ')
# print(f'Você acabou de digitar o número {numeroInteiro}')

numeroFloat = leiaFloat('Digite um número float: ')
print(f'Você digitou o número float {numeroFloat}')