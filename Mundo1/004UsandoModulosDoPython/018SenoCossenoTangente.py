# Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math

angulo = float(input('Informe um angulo: '))
anguloEmRadiandos = math.radians(angulo)
seno = math.sin(anguloEmRadiandos)
cosseno = math.cos(anguloEmRadiandos)
tangente = math.tan(anguloEmRadiandos)
print('O seno é {:.2f} o cosseno é {:.2f} a tangente é {:.2f}'.format(seno, cosseno, tangente))