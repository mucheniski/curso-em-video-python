# Exercício Python 094: Crie um programa que leia nome, sexo e idade de várias pessoas,
# guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

listaDicionariosPessoas = list()
pessoa = dict()

while True:

    pessoa['nome'] = str(input('Informe o nome: ')).strip()
    pessoa['sexo'] = str(input('Informe o sexo M ou F')).strip().upper()
    pessoa['idade'] = int(input('Informe a idade: '))

    listaDicionariosPessoas.append(pessoa.copy())
    pessoa.clear()

    resposta = str(input('Deseja continuar? S ou N: ')).strip().upper()
    while resposta not in 'SN':
        resposta = str(input('Valor incorreto, deseja continuar? S ou N: ')).strip().upper()

    if resposta == 'N':
        break
print('Fim do programa')

# listaDicionariosPessoas = [
#     {'nome': 'Diego', 'sexo': 'M', 'idade': 35},
#     {'nome': 'Bruna', 'sexo': 'F', 'idade': 30},
#     {'nome': 'Lorena', 'sexo': 'F', 'idade': 23}
# ]

mediaIdade = somaIdades = quantidadePessoas = 0
listaMulheres = list()
listaIdadeAcimaDaMedia = list()

quantidadePessoas = len(listaDicionariosPessoas)

for pessoas in listaDicionariosPessoas:
    for key, value in pessoas.items():
        print(f'Chave {key} valor {value}')
        if key == 'idade':
            somaIdades += value

        if key == 'sexo' and value == 'F':
                listaMulheres.append(pessoas)

print(f'A) Quantas pessoas foram cadastradas {quantidadePessoas}')

mediaIdade = somaIdades / quantidadePessoas
print(f'B) A média de idade {mediaIdade:.2f}')

print(f'C) Uma lista com as mulheres {listaMulheres}')

for pessoas in listaDicionariosPessoas:
    for key, value in pessoas.items():
        if key == 'idade' and value > mediaIdade:
            listaIdadeAcimaDaMedia.append(pessoas)

print(f'D) Uma lista de pessoas com idade acima da média {listaIdadeAcimaDaMedia}')