# Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da
# Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense.
times = ('Curinthia', 'Parmera', 'Chapecoense', 'São Paulo', 'Santos', 'Fluminense', 'Flamengo')
print('='*100)
print('# a) Os 5 primeiros times.')
print(times[0:2])

print('='*100)
print('# b) Os últimos 2 colocados.')
print(times[-2:])

print('='*100)
print('# c) Times em ordem alfabética.')
print(sorted(times))

print('='*100)
print('# d) Em que posição está o time da Chapecoense.')
print(times.index('Chapecoense'))
print('='*100)