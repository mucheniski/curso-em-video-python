termo = int(input('Informe o termo: '))
razao = int(input('Informe a razão: '))

# Enésimo termo de uma razão
decimo = termo + (10 - 1) * razao

for i in range(termo, decimo + razao, razao):
    print('{} '.format(i), end=' -> ')
print('ACABOU!')
