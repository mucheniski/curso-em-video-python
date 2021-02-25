numero = int(input('Informe o número: '))
cont = 1

while cont <= 10:
    print('{} x {} = {}'.format(numero, cont, (numero * cont)))
    cont += 1