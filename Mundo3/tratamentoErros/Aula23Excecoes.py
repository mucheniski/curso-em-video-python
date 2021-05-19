# else e finally são opcionais
try:
    a = 1
    b = 0
    r = a / b
except TypeError as erro:
    print(f'Erro de tipo {erro.__class__}')
except ZeroDivisionError as erro:
    pritn(f'Erro divido por zero {erro.__class__}')
except Exception as erro:
    print(f'Moio deu erro {erro.__class__}')
else:
    print(f'O Resultado é {r}')
finally:
    print('Fim do programa')