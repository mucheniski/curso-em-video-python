# A tupla é criada com parênteses
# Tuplas são imutáveis, não pode se atribuir valores depois de iniciada
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print('='*100)
print(lanche)
print(lanche[1])
print(lanche[-1])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])

print('='*100)
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Meodeos comi demais!')

print('='*100)
print(len(lanche))

print('='*100)
for i in range(0, len(lanche)):
    print(f'Comi com len agora {lanche[i]}')

print('='*100)
for posicao, comida in enumerate(lanche):
    print(f'Comi com enumerate {posicao} - {comida}')

print('='*100)
print('Em ordem alfabética: ', sorted(lanche))

print('='*100)
a = (4, 1, 7, 5)
b = (3, 5, 10)
c = a + b
d = b + a
print(c)
print(d)
print(c.count(5))
print(c.index(3))
# sempre retorna a primeira ocorrencia, no caso como tem 2 x o numero 5, se eu quiser pegar a segunda ocorrência:
# print(c.index(de, a partir da posição x))
print(c.index(5,4))

print('='*100)

# Na tupla aceita dados de tipos diferentes
pessoa = ('Diego', 34, 1.74)
print(pessoa)

# apagar tupla, retira da memória a tupla completa, um elemento não pode ser deletado, apenas a tupla toda
del(pessoa)