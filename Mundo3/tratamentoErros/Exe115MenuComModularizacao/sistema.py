from lib.interface import *
from time import sleep

while True:
    resposta = menu(['Criar', 'Editar', 'Sair'])
    if resposta == 1:
        print('Opção 1')
    elif resposta == 2:
        print('Opção 2')
    elif resposta == 3:
        print('Saindo')
        break
    else:
        print('Digite uma opção válida')
    sleep(2)


