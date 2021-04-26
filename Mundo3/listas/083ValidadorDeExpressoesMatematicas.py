# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.
expressao = str(input('Informe a expressão: '))
contAbertos = contFechados = 0
for letra in expressao:
    if letra == '(':
        contAbertos += 1
    if letra == ')':
        contFechados += 1

if contAbertos == contFechados:
    print('Válida')
else:
    print('Inválida')