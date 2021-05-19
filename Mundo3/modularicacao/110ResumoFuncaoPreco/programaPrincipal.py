import moeda

valor = 10.15
print(moeda.formataValor(valor))
print(moeda.dobroPreco(valor))
print(moeda.metadeDoPreco(valor))
print(moeda.percentual(valor, 10))
print()
print('='*100)


moeda.resumo(valor, 10, 20)