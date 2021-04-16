listaNumeros = [4,6,8,3,4,6,5,1,4]
print(listaNumeros)

print('-'*100)
print('substituir um valor listaNumeros[2] = 0')
listaNumeros[2] = 0
print(listaNumeros)

print('-'*100)
print('Adicionar um valor listaNumeros.append(10)')
listaNumeros.append(10)
print(listaNumeros)

print('-'*100)
print('Ordenar os numeros em ordem crescente listaNumeros.sort()')
listaNumeros.sort()
print(listaNumeros)

print('-'*100)
print('Ordenar os numeros em ordem decrescente listaNumeros.sort(reverse=True)')
listaNumeros.sort(reverse=True)
print(listaNumeros)

print('-'*100)
print('Ver a quantidade de elementos len(listaNumeros)')
print(len(listaNumeros))

print('-'*100)
print('Inserir em um local específico listaNumeros.insert(posicao, valor) listaNumeros.insert(2,0)')
print(listaNumeros)
listaNumeros.insert(2,0)
print(listaNumeros)

print('-'*100)
print('Remover com pop listaNumeros.pop(2), sem parametros elimina o último valor')
listaNumeros.pop(2)
print(listaNumeros)
listaNumeros.pop()
print(listaNumeros)

print('-'*100)
print('Remover o um elemento com remove voce passa o valor, não a posição')
print(listaNumeros)
listaNumeros.remove(6)
print(listaNumeros)

print('-'*100)
if 7 in listaNumeros:
    listaNumeros.remove(7)
else:
    print('Não achei o número')

print('-'*100)
print('Nova lista')
valores = list()
valores.append(4)
valores.append(5)
valores.append(7)

for valor in valores:
    print(f'{valor}...', end='')

print('-'*100)
for chave, valor in enumerate(valores):
    print(f'na chave {chave} tem o valor {valor}')

print('-'*100)
novosValores = list()

# for i in range(0, 3):
#     novosValores.append(int(input('Informe um valor: ')))
# print(novosValores)


print('-'*100)
lista1 = [2, 4, 6, 8]
print('sempre que iguala uma lista na outra o python cria uma ligação, quando for alterada uma lista a outra também é')
lista2 = lista1
print(f'lista1 {lista1}')
print(f'lista2 {lista2}')
lista2[2] = 3
print('foi alterado')
print(f'lista1 {lista1}')
print(f'lista2 {lista2}')

print('-'*100)
lista1 = [2, 4, 6, 8]
print('Se quiser que receba uma cópia dos valores, é feito assim')
lista2 = lista1[:]
print(f'lista1 {lista1}')
print(f'lista2 {lista2}')
lista2[2] = 3
print('não foi alterado')
print(f'lista1 {lista1}')
print(f'lista2 {lista2}')
