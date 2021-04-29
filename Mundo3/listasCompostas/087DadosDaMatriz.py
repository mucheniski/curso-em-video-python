# Exercício Python 087: Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matriz = [[0,0,0],[0,0,0],[0,0,0]]
somaPares = somaTerceiraColuna = maiorValorSegundaLinha = 0

for linha in range(0,3):
    for coluna in range(0,3):
        valor = int(input(f'Informe o valor para [{linha}][{coluna}]: '))
        matriz[linha][coluna] = valor

        if valor % 2 == 0:
            somaPares += valor

        if coluna == 2:
            somaTerceiraColuna += valor

        if linha == 1:
            if coluna == 0:
                maiorValorSegundaLinha = valor
            else:
                if valor > maiorValorSegundaLinha:
                    maiorValorSegundaLinha = valor


print('='*50)
for linha in range(0,3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()

print('='*50)
print(f'# A) A soma de todos os valores pares digitados. {somaPares}')
print(f'# B) A soma dos valores da terceira coluna. {somaTerceiraColuna}')
print(f'# C) O maior valor da segunda linha. {maiorValorSegundaLinha}')