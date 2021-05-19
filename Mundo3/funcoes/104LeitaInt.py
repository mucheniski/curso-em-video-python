# Exercício Python 104: Crie um programa que tenha a função leiaInt(),
# que vai funcionar de forma semelhante ‘a função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaInt(mensgem):
    numero = 0
    while True:
        numero = str(input(mensgem))
        if numero.isnumeric():
            numero = int(numero)
            break
        else:
            print('\033[0:31mERRO! Informe um número válido!\033[m')
    return numero


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
