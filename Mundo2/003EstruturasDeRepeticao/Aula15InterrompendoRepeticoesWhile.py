numero = soma = 0
while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    soma += numero
# print('A soma é {}'.format(soma))

# Print com fstring a partir da versão 3 do python
print(f'A soma é {soma}')

nome = 'Diego'
idade = 34
salario = 18000.00
print(f'o {nome} tem {idade} anos e ganha RS{salario:.2f}')