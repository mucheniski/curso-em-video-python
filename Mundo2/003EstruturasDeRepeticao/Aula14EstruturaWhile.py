n = 1
while n < 10:
    print(n)
    n += 1
print('Fim')

while n != 0:
    n = int(input('Informe o valor: '))
print('Fim')

continuar = 'S'
pares = 0
impares = 0
while continuar == 'S':
    numero = int(input('Informe um número: '))
    if numero % 2 == 0:
        pares += 1
    else:
        impares +=1
    continuar = str(input('Deseja continuar? S/N ')).upper().strip()
print('Fim da programação {} pares e {} impares'.format(pares, impares))