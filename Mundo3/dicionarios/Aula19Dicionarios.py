pessoas = {'nome': 'Diego', 'sexo': 'M', 'idade': 34}
print(pessoas)
print(pessoas['nome'])

# Quando quiser fazer print formatado, como está dentro de aspas simples, precisamos referencias
# os elementos com aspas duplas
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

for key, value in pessoas.items():
    print(key)

# apagar
del pessoas['sexo']

# Trocando o nome
pessoas['nome'] = 'Mucheniski'

# Adicionando elementos
pessoas['peso'] = 65.0

brasil = []
estado1 = {'nome': 'Paraná', 'sigla': 'PR'}
estado2 = {'nome': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil)
print(brasil[0]['nome'])

print('-'*100)
estado3 = {}
brasil = list()

for i in range(0, 3):
    estado3['uf'] = str(input('Informe a uf: '))
    estado3['sigla'] = str(input('Informe a sigla: '))
    brasil.append(estado3.copy())
print(brasil)
for estados in brasil:
    for key, value in estados.items():
        print(f'O campo {key} tem valor {value}')