# Exercício Python 53: Crie um programa que leia uma frase qualquer
# e diga se ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:
#
# APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

# strip remove os espaços no início e no fim da frase
# frase = str(input('Digite uma frase: ')).strip().upper()
frase = 'APOS A SOPA'.strip().upper()
print('Frase digitada {}'.format(frase))

palavras = frase.split()
print('Separada em palavras {}'.format(palavras))

junto = ''.join(palavras)
print('Tudo junto sem espaços {}'.format(junto))

print('Tamanho da frase {}'.format(len(junto)))

# Forma mais simples
inverso = junto[::-1]

# inverso = ''
# # Lendo de traz pra frente, le da última posição até a primeira voltando de um em um
# for letra in range(len(junto) -1, -1, -1):
#     # print(junto[letra])
#     inverso += junto[letra]

print('Palavra invertida {}'.format(inverso))

if inverso == junto:
    print('Temos um palíndromo')
else:
    print('Não é um palíndromo')