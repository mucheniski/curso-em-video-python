# Exercício Python 078: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista = list()
maior = menor = 0
for i in range (0, 5):
    valor = int(input('Informe um valor: '))
    lista.append(valor)
    if i == 0:
        maior = valor
        menor = valor
    else:
       if valor > maior:
            maior = valor
       if valor < menor:
            menor = valor

print(f'Os valores digitados foram {lista}')
print(f'O menor valor é {menor} e o maior valor é {maior}')