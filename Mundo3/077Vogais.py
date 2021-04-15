# Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
palavras = ('Longing', 'rusted', 'seventeen', 'daybreak', 'furnace', 'nine', 'benign', 'homecoming', 'one', 'freight car')
for palavra in palavras:
    print(f'em {palavra} temos: ')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
    print()
    print('-'*50)