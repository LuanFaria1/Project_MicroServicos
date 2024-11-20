# Dados de exemplo para professores, alunos e disciplinas
professores = [
    {'nome': "joao", 'id_professor': 1},
    {'nome': "jose", 'id_professor': 2},
    {'nome': "maria", 'id_professor': 3}
]

alunos = [
    {'nome': "alexandre", 'id_aluno': 1},
    {'nome': "miguel", 'id_aluno': 2},
    {'nome': "janaina", 'id_aluno': 3},
    {'nome': "cicero", 'id_aluno': 4},
    {'nome': "dilan", 'id_aluno': 5}
]

disciplinas = [
    {'nome': "apis e microservicos", 'id_disciplina': 1, 'alunos': [1, 2, 3, 4], 'professores': [1], 'publica': False},
    {'nome': "matematica financeira", 'id_disciplina': 2, 'alunos': [2], 'professores': [3], 'publica': True},
    {'nome': "matematica basica", 'id_disciplina': 3, 'alunos': [1, 2], 'professores': [3, 2], 'publica': False}
]

class DisciplinaNaoEncontrada(Exception):
    pass

def listar_professores():
    return professores

def listar_alunos():
    return alunos

def leciona(id_professor, id_disciplina):
    """Verifica se um professor leciona uma disciplina específica."""
    for disciplina in disciplinas:
        if disciplina['id_disciplina'] == id_disciplina:
            return id_professor in disciplina['professores']
    raise DisciplinaNaoEncontrada
