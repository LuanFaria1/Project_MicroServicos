import requests

def verifica_leciona(id_professor, id_disciplina):
    try:
        r = requests.get(f"http://localhost:5001/leciona/{id_professor}/{id_disciplina}")
        if r.status_code == 404:
            return False, 'Disciplina não encontrada'
        return r.json().get('leciona', False)
    except requests.RequestException as e:
        return False, f"Erro na comunicação com pessoa_service: {e}"
