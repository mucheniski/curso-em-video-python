# importando somente alguns objetos
# quando importado dessa forma não preciso mais referenciar math.sqrt já chamo direto
from math import sqrt, ceil, floor

numero = int(input('Digite um número: '))
raizQuadrada = sqrt(numero)
print('A raiz de {} é igual a {}'.format(numero, raizQuadrada))
print('A raiz arredondada para cima é {}'.format(ceil(raizQuadrada)))
print('A raiz arredondada para baixo é {}'.format(floor(raizQuadrada)))