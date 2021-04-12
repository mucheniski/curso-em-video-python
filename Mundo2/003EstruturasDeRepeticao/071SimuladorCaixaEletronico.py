valor = int(input('Qual valor deseja sacar? '))
total = valor
cadulaAtual = 50
contCedulas = 0

while True:
    if total >= cadulaAtual:
        total -= cadulaAtual
        contCedulas += 1
    else:
        if contCedulas > 0:
            print(f'{contCedulas} cedulas de R${cadulaAtual}')
        if cadulaAtual == 50:
            cadulaAtual = 20
        elif cadulaAtual == 20:
            cadulaAtual = 10
        elif cadulaAtual == 10:
            cadulaAtual = 1

        contCedulas = 0

        if total == 0:
            break
print('Finalizado')

