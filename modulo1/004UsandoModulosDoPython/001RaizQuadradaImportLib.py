# importando toda a lib math
import math

numero = int(input('Digite um número: '))
raizQuadrada = math.sqrt(numero)
print('A raiz de {} é igual a {}'.format(numero, raizQuadrada))
print('A raiz arredondada para cima é {}'.format(math.ceil(raizQuadrada)))
print('A raiz arredondada para baixo é {}'.format(math.floor(raizQuadrada)))