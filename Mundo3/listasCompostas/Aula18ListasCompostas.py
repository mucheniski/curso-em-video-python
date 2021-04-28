# [:] significa cópia da lista, se eu fizer apenas o append, uma lista vai estar relacionada a outra
pessoa = list()
pessoa.append('Diego')
pessoa.append(34)

galera = list()
galera.append(pessoa[:])
print(galera)
pessoa[0] = 'Bruna'
pessoa[1] = '30'
galera.append(pessoa[:])
print(galera)

galera2 = [['Dirce',54],['Laurindo',65],['Pati',27]]
print(galera2[0])
print(galera2[2][1])

for pessoa in galera2:
    print(pessoa)

for pessoa in galera2:
    print(f'{pessoa[0]} tem {pessoa[1]} anos')

totalMaiores = totalMenores = 0
for pessoa in galera2:
    if pessoa[1] >= 21:
        print(f'{pessoa[0]} é maior de idade')
        totalMaiores += 1
    else:
        print(f'{pessoa[0]} é menor de idade')
        totalMenores += 1

print(f'Temos {totalMaiores} maiores e {totalMenores} menores')



dado = list()
galera3 = list()

# for i in range(0,3):
#     dado.append(str(input('Informe o nome: ')))
#     dado.append(int(input('Informe a idade: ')))
#     galera3.append(dado[:])
#     dado.clear()
#
# print(galera3)