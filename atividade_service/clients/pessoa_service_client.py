import requests

PESSOA_SERVICE_URL = "http://localhost:5001/pessoas"

class PessoaServiceClient:
    @staticmethod
    def verificar_leciona(id_professor, id_disciplina):
        url = f"{PESSOA_SERVICE_URL}/leciona/{id_professor}/{id_disciplina}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data.get('leciona', False) if data.get('isok') else False
        except requests.RequestException as e:
            print(f"Erro ao acessar o pessoa_service: {e}")
            return False
