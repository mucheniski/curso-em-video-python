print('Tabuada')
for i in range(1,11):
    cont = 2
    print("{} x {} = {}".format(cont, i, (i * cont)))
    cont += 1;
print("-"*50)

# Sempre no último ele para, nesse caso vai imprimir 5 vezes
for i in range(1, 6):
    print(i)
print('Fim')
print("-"*50)

print('Contando de traz pra frente')
for i in range(6, 0, -1): # O range de -1 faz ele decrementar o número
    print(i)
print('Fim')
print("-"*50)

print('Pulando de 2 em 2')
for i in range(0, 7, 2):
    print(i)
print('Fim')
print('-'*50)

n = int(input('Digite um número: '))
for i in range(0, n):
    print(i)
print('Fim')
print('-'*50)

inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
for i in range(inicio, fim+1, passo):
    print(i)
print('Fim')
print('-'*50)
