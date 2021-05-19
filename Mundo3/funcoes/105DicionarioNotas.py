# Exercício Python 105: Faça um programa que tenha uma função notas()
# que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

def notas(* listaNotas, mostraSituacao=False):
    dicionario = dict()
    maiorNota = menorNota = somaNotas = totalNotas = 0
    primeiraNota = True
    situacao = 'APROVADO'

    # – Quantidade de notas
    dicionario['Total notas'] = len(listaNotas)
    dicionario['Maior nota'] = max(listaNotas)
    dicionario['Menor nota'] = min(listaNotas)
    dicionario['Média'] = sum(listaNotas) / len(listaNotas)

    # – A situação (opcional)
    if mostraSituacao:
        if dicionario['Média'] > 5 and dicionario['Média'] <= 7:
            situacao = 'RECUPERAÇÃO'
        if dicionario['Média'] < 5:
            situacao = 'REPROVADO'

        dicionario['Situação'] = situacao

    return dicionario


print(notas(10, 8, 9.5, mostraSituacao=True))