# Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho
# e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO,
# o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade,
# com quantos anos a pessoa vai se aposentar.
import datetime

anoAtual = datetime.date.today().year

idadeAtual = idadeAposentadoria = anoDaAposentadoria = anosParaAposentar = 0

dadosPessoais = dict()

dadosPessoais['nome'] = str(input('Informe o nome: ')).strip()

anoNascimento = int(input('Informe o ano de nascimento: '))
idadeAtual = anoAtual - anoNascimento
dadosPessoais['idade'] = idadeAtual

dadosPessoais['numeroCTPS'] = int(input('Informe o número da CTPS 0 para vazio: '))

if dadosPessoais['numeroCTPS'] != 0:
    dadosPessoais['anoContratacao'] = int(input('Informe o ano de contratação: '))
    dadosPessoais['salario'] = float(input('Informe o salário: '))

    anoDaAposentadoria = dadosPessoais['anoContratacao'] + 35
    anosParaAposentar = anoDaAposentadoria - anoAtual
    idadeAposentadoria = idadeAtual + anosParaAposentar

print(dadosPessoais)
print(f'Vodê vai se aposentar com {idadeAposentadoria} anos')

