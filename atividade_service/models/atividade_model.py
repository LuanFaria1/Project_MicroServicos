atividades = [
    {
        'id_atividade': 1,
        'id_disciplina': 1,
        'enunciado': 'Crie um app de todo em Flask',
        'respostas': [
            {'id_aluno': 1, 'resposta': 'todo.py', 'nota': 9},
            {'id_aluno': 2, 'resposta': 'todo.zip.rar'},
            {'id_aluno': 4, 'resposta': 'todo.zip', 'nota': 10}
        ]
    },
    {
        'id_atividade': 2,
        'id_disciplina': 1,
        'enunciado': 'Crie um servidor que envia email em Flask',
        'respostas': [
            {'id_aluno': 4, 'resposta': 'email.zip', 'nota': 10}
        ]
    }
]

class AtividadeNotFound(Exception):
    pass

def listar_atividades():
    return atividades

def obter_atividade(id_atividade):
    for atividade in atividades:
        if atividade['id_atividade'] == id_atividade:
            return atividade
    raise AtividadeNotFound

def criar_atividade(nova_atividade):
    nova_atividade['id_atividade'] = max([a['id_atividade'] for a in atividades] or [0]) + 1
    atividades.append(nova_atividade)
    return nova_atividade

def atualizar_atividade(id_atividade, dados_atualizados):
    for atividade in atividades:
        if atividade['id_atividade'] == id_atividade:
            atividade.update(dados_atualizados)
            return atividade
    raise AtividadeNotFound

def deletar_atividade(id_atividade):
    global atividades
    atividades = [a for a in atividades if a['id_atividade'] != id_atividade]
    if not any(a['id_atividade'] == id_atividade for a in atividades):
        return True
    raise AtividadeNotFound
