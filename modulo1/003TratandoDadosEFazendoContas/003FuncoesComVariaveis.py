algoDigitado = input('Digite algo : ')
print('É numerico? ', algoDigitado.isnumeric())        # Se é possível converter o valor digitado em númerico, retorna True ou False
print('É alfabético? ', algoDigitado.isalpha())          # Se é alfabético ou seja, somente letras
print('É alfanumérico? ', algoDigitado.isalnum())          # Se é alfanumérico, letras ou números 
print('Está em maiúscula? ', algoDigitado.isupper())          # Se tem somente letras maiúsculas
print('É espaço? ', algoDigitado.isspace())
print('Está capitalizado? ', algoDigitado.istitle)
