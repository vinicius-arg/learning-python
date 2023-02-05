'''Testes em OO'''

class Aluno:
    def __init__(self, name, grade, situation):
        self.name = name
        self.grade = grade
        self.situation = situation

def approved(g):
    if g >= 7:
        return 'APROVADO'
    elif g >= 5:
        return 'RECUPERAÇÃO'
    else:
        return 'REPROVADO'

name = input('Digite o nome do aluno: ')
grade = float(input('Digite a nota do aluno: '))
situation = approved(grade)

aluno = Aluno(name, grade, situation)

print(f'{aluno.name} ficou com média final de {aluno.grade} e sua situação é {aluno.situation}.')
