frase = 'Curso em Vídeo Python'

# C u r s o   e m   V í  d  e  o     P  y  t  h  o  n
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

print('Pegando apenas a letra no indice 9 ',frase[9])
print('Pegando de 9 a 13, o ultimo é excluído ', frase[9:13])
print('Do 9 ao 20 pulando de 2 em 2 ', frase[9:21:2])
print('Do caractere zero até 5, sempre exclui o último ', frase[:5])
print('Do 15 até o final ', frase[15:])
print('Do 9 até o final pulando de 3 em 3 ', frase[9::3])
print('='*50)
print('Tamanho da frase ', len(frase))
print('Contar quantas vezes aparece o o minúsculo ', frase.count('o'))
print('Contar do 0 até o 13 quantas vezes aparece o ', frase.count('o',0,13))
print('Mostrar quantas vezes encontrou deo, onde começa ', frase.find('deo'))
print('Buscar uma string que não existe, deve retornar menos um ', frase.find('rute'))
print('Boolean se existe a frase ', 'Curso' in frase)
#Nesse caso o próprio Python cria um novo array com mais caracteres para caber Android
#para alterar a frase é preciso fazer frase = frase.replace
print('Substituindo palavras ', frase.replace('Python', 'Android'))
print('Imprimindo em maiúscula ', frase.upper())
print('Imprimindo em minúsculo ', frase.lower())
print('Deixando só o primeiro caracter em maiusculo ', frase.capitalize())
print('Sempre depois do espaço deixa a primeira maiúscula ', frase.title())
print('='*50)
frase2 = '   Frase com espaços   '
print('Removendo todos os espaços inúteis do começo e do fim da frase ', frase2.strip())
print('Removendo espaços da direita ', frase2.rstrip())
print('Removendo espaços da esquerda ', frase2.lstrip())
print('='*50)
frase3 = 'Curso em Vídeo Python'
print('Dividir as strings por espaços ', frase3.split())
print('Juntar nomes separados em listas ', '-'.join(frase3))