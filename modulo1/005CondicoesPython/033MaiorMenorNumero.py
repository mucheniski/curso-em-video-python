a = int(input('Informe o primeiro número: '))
b = int(input('Informe o segundo número: '))
c = int(input('Informe o terceiro número: '))
maiorValor = a
menorValor = a

print('Numeros informados {}, {} e {}'.format(a, b, c))

# Verificando o menor valor
if b < a and b < c:
    menorValor = b
if c < a and c < b:
    menorValor = c

# Verificando o maior valor
if b > a and b > c:
    maiorValor = b
if c > a and c > b:
    maiorValor = c

print('O maior valor é {}'.format(maiorValor))
print('O menor valor é {}'.format(menorValor))